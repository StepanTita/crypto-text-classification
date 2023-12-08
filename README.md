# Crypto Text Classification 🚀

**Predicting cryptocurrency price movements** through Natural Language Processing (NLP) and transformer models.

## Overview 🔍

The **crypto-text-classification** repository explores the application of NLP techniques, particularly leveraging
transformer models, to predict the impact of news articles on Bitcoin prices. This research aims to address the
volatility of cryptocurrency markets by fine-tuning **BERT**, a pre-trained transformer model, on a small manually
labeled dataset of 1800 news pieces. Additionally, it expands the dataset by automatically labeling an additional 1000
news articles using a custom **Bing API** and **Bing GPT**.

## Objectives ✅

- **Predict labeled data with BERT**
- **Predict unlabeled data with Bing API or GPT-4**
- **Predict soft-labeled data with BERT and validate performance improvements**

## How to Use ⚙️

1. **Split labeled data** into two subsets (50:50)
2. **Fine-tune BERT** on labeled 50% of the data
3. **Evaluate BERT** on the remaining labeled 50% of the data
4. **Label crypto-news** with GPT
5. **Train BERT** with labeled + soft-labeled data
6. **Evaluate** on the remaining labeled 50% of the data

## Baseline Results 🧸

### TF-IDF Vectorization 📚

| Model             | Precision | Recall   | F1-Score | Accuracy |
|-------------------|-----------|----------|----------|----------|
| Nearest Neighbors | 0.65      | 0.67     | 0.66     | 0.67     |
| Linear SVM        | 0.69      | 0.68     | 0.60     | 0.68     |
| RBF SVM           | **0.72**  | **0.73** | **0.70** | **0.73** |
| Gaussian Process  | 0.70      | 0.71     | 0.68     | 0.71     |
| Decision Tree     | 0.59      | 0.61     | 0.59     | 0.61     |
| Random Forest     | 0.70      | 0.71     | 0.67     | 0.71     |
| Neural Net        | 0.68      | 0.69     | 0.67     | 0.69     |
| AdaBoost          | 0.70      | 0.70     | 0.65     | 0.70     |
| QDA               | 0.69      | 0.68     | 0.68     | 0.68     |

### Open-AI Base-Models 🌐

| Model | Accuracy | Precision | Recall | AUROC | AUPRC | F1   |
|-------|----------|-----------|--------|-------|-------|------|
| ada   | 0.70     | 0.72      | 0.89   | 0.74  | 0.84  | 0.80 |

### BERT-base-cased 🧩

```python
MODEL_NAME = 'bert-base-cased'
NUM_LABELS = 2

NUM_EPOCHS = 1
BATCH_SIZE = 32
MAX_SEQ_LEN = 512
LEARNING_RATE = 2e-5
MAX_GRAD_NORM = 1000
```

| Model           | Accuracy | Precision | Recall | AUROC | AUPRC | F1   |
|-----------------|----------|-----------|--------|-------|-------|------|
| BERT-base-cased | 0.66     | 0.44      | 0.66   | 0.50  | 0.34  | 0.53 |

## After Augmentation 🛠

### Traditional ML 📚

| Model             | Precision | Recall   | F1-Score | Accuracy |
|-------------------|-----------|----------|----------|----------|
| Nearest Neighbors | 0.59      | 0.62     | 0.59     | 0.62     |
| Linear SVM        | **0.68**  | **0.68** | 0.62     | **0.68** |
| RBF SVM           | 0.65      | 0.67     | **0.64** | 0.67     |
| Gaussian Process  | 0.64      | 0.66     | **0.64** | 0.66     |
| Decision Tree     | 0.63      | 0.65     | 0.63     | 0.65     |
| Random Forest     | 0.65      | 0.67     | 0.63     | 0.67     |
| Neural Net        | 0.62      | 0.64     | 0.62     | 0.64     |
| AdaBoost          | 0.62      | 0.63     | 0.62     | 0.63     |
| QDA               | 0.63      | 0.61     | 0.62     | 0.61     |

### Open AI models 🌐

| Model | Accuracy | Precision | Recall | AUROC | AUPRC | F1   |
|-------|----------|-----------|--------|-------|-------|------|
| ada   | 0.66     | 0.72      | 0.73   | 0.69  | 0.76  | 0.72 |

### BERT-base-cased 🧩

| Model           | Accuracy | Precision | Recall | AUROC | AUPRC | F1   |
|-----------------|----------|-----------|--------|-------|-------|------|
| BERT-base-cased | 0.66     | 0.44      | 0.66   | 0.50  | 0.34  | 0.53 |

## Conclusion

This research establishes a proof of concept for **predicting cryptocurrency price movements** based on news sentiment
analysis. The results demonstrate the effectiveness of transformer models, particularly **BERT**, in enhancing
prediction accuracy and robustness.

Feel free to contribute and improve this project! 🌐📈

### Collect cookies

1. Get a browser that looks like Microsoft Edge.

- a) (Easy) Install the latest version of Microsoft Edge
- b) (Advanced) Alternatively, you can use any browser and set the user-agent to look like you're using Edge (
  e.g., `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51`).
  You can do this easily with an extension like "User-Agent Switcher and Manager"
  for [Chrome](https://chrome.google.com/webstore/detail/user-agent-switcher-and-m/bhchdcejhohfmigjafbampogmaanbfkg)
  and [Firefox](https://addons.mozilla.org/en-US/firefox/addon/user-agent-string-switcher/).

2. Open [bing.com/chat](https://bing.com/chat)
3. If you see a chat feature, you are good to continue...
4. Install the cookie editor extension
   for [Chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm)
   or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)
5. Go to [bing.com](https://bing.com)
6. Open the extension
7. Click "Export" on the bottom right, then "Export as JSON" (This saves your cookies to clipboard)
8. Paste your cookies into a file `bing_cookies_main.json`.

[//]: # (   - NOTE: The **cookies file name MUST follow the regex pattern `bing_cookies_*.json`**, so that they could be recognized by internal cookie processing mechanisms)
