import asyncio
import json
import random
import time

import numpy as np
import pandas as pd
from EdgeGPT.EdgeGPT import Chatbot, ConversationStyle
from tqdm import tqdm

from scripts.logger import logger
from scripts.retry import retry_with_exponential_backoff, log_continue

"""
{
    "text": str,
    "author": str,
    "sources": list[dict],
    "sources_text": str,
    "suggestions": list[str],
    "messages_left": int
}
"""


@log_continue
@retry_with_exponential_backoff(tries=5)
async def generate_output(bot, text):
    return await bot.ask(prompt=f"""Based on the provided piece of news, search the web, and find evidence, if this news affected the price of the cryptocurrency or not.
            If it did, then just output: [effect:1], otherwise just output: [effect:0]. Only output the result, without explanations. Try to be very concise.

            News:
            {text}""", conversation_style=ConversationStyle.creative,
                         simplify_response=True)


@retry_with_exponential_backoff(tries=5)
async def renew_bot():
    return await Chatbot.create(cookies=None)


async def generate_labels(data, cookies, save_rate=5, start_index=0, max_count=300):
    logger.info('Generating labels...')
    bot = await Chatbot.create(cookies=cookies)  # Passing cookies is "optional"

    # data['label'] = None
    data['label_text'] = data.get('label_text', np.nan)
    data['label_sources_text'] = data.get('label_sources_text', np.nan)

    count = 0

    try:
        for i, text in tqdm(data['text'].items(), total=min(max_count, len(data))):
            if i < start_index:
                continue

            if count >= max_count:
                break

            response = await generate_output(bot, text)

            if response is None or \
                    not isinstance(response, dict) \
                    or len({'messages_left', 'text', 'sources_text'} - set(response.keys())) != 0:
                logger.warning('Response format is inappropriate')
                logger.warning(response)

                logger.warning('Refreshing Bot State...')
                await bot.close()
                bot = await renew_bot()
                continue

            if response['messages_left'] == 0:
                logger.info('Refreshing Bot State...')
                await bot.close()
                bot = await renew_bot()

            data['label_text'].iloc[i] = response['text']
            data['label_sources_text'].iloc[i] = response['sources_text']

            if (i + 1) % save_rate == 0:
                logger.info('Dumping Data...')
                data.to_csv('./output/classification/crypto_news_plus_2.csv', index=False)

            count += 1
            time.sleep(random.uniform(a=1, b=10))
    except Exception as e:
        logger.fatal(e)
    finally:
        logger.info('Dumping Data...')
        data.to_csv('./output/classification/crypto_news_plus_2.csv', index=False)

    # print(json.dumps(response, indent=2))  # Returns
    await bot.close()


def main():
    cookies = json.loads(open("./bing_cookies_main.json", encoding="utf-8").read())

    # cookies = None

    data = pd.read_csv('./output/classification/crypto_news_plus_2.csv')

    asyncio.run(generate_labels(data, cookies, start_index=0, max_count=300))


if __name__ == "__main__":
    main()
