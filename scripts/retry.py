import random
import time
import traceback
from functools import wraps

from scripts.logger import logger


def log_continue(fn):
    async def wrapped(*args, **kwargs):
        try:
            return await fn(*args, **kwargs)
        except Exception as e:
            traceback.print_exception(e)
            logger.error(str(e))
            return None

    return wrapped

def retry_with_exponential_backoff(tries=10, delay=3, backoff=2, max_delay=15 * 60):
    """Retry calling the decorated function using an exponential backoff.

    http://www.saltycrane.com/blog/2009/11/trying-out-retry-decorator-python/
    original from: http://wiki.python.org/moin/PythonDecoratorLibrary#Retry
    :param tries: number of times to try (not retry) before giving up
    :type tries: int
    :param delay: initial delay between retries in seconds
    :type delay: int
    :param backoff: backoff multiplier e.g. value of 2 will double the delay
        each retry
    :type backoff: int
    :param max_delay: max delay that can be reached in seconds
    :type max_delay: int
    """

    def deco_retry(f):

        @wraps(f)
        async def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay
            while mtries > 1:
                try:
                    return await f(*args, **kwargs)
                except Exception as err:
                    msg = f"{str(err)}, Retrying in {mdelay} seconds..."

                    logger.warning(msg)
                    # adding random uniform delay to each sleep time to exclude any multiple requests synchronization
                    time.sleep(mdelay + random.uniform(a=1, b=10))
                    mtries -= 1
                    mdelay *= backoff
                    mdelay = min(mdelay, max_delay)
            return await f(*args, **kwargs)

        return f_retry  # true decorator

    return deco_retry
