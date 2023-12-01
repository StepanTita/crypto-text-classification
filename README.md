# crypto-text-classification

**TODO:**

- Predict labelled data with BERT
- Predict unlabelled data with Bing API (or GPT-4???)
- Predict soft labelled data with BERT and validate if the performance improves

**HOWTO:**

- Split labelled data into 2 subsets 50:50
- Fine-tune BERT on labelled 50% of the data
- Evaluate BERT on remaining labelled 50% of the data
- Label crypto-news with GPT
- Train BERT with labelled + soft-labelled data
- Evaluate on the remaining labelled 50% of the data

## Baseline:

(2-class classification 0 - not important news, 1 - important)

### TF-IDF vectorization

_(description only)_

```
Nearest Neighbors
              precision    recall  f1-score   support

           0       0.71      0.83      0.76       262
           1       0.53      0.36      0.43       139

    accuracy                           0.67       401
   macro avg       0.62      0.59      0.60       401
weighted avg       0.65      0.67      0.65       401
```

```
Linear SVM
              precision    recall  f1-score   support

           0       0.68      0.97      0.80       262
           1       0.70      0.14      0.23       139

    accuracy                           0.68       401
   macro avg       0.69      0.55      0.51       401
weighted avg       0.69      0.68      0.60       401
```

```
RBF SVM
              precision    recall  f1-score   support

           0       0.73      0.92      0.81       262
           1       0.70      0.37      0.49       139

    accuracy                           0.73       401
   macro avg       0.72      0.65      0.65       401
weighted avg       0.72      0.73      0.70       401
```

```
Gaussian Process
              precision    recall  f1-score   support

           0       0.72      0.92      0.81       262
           1       0.67      0.32      0.44       139

    accuracy                           0.71       401
   macro avg       0.70      0.62      0.62       401
weighted avg       0.70      0.71      0.68       401
```

```
Decision Tree
              precision    recall  f1-score   support

           0       0.68      0.76      0.71       262
           1       0.41      0.32      0.36       139

    accuracy                           0.61       401
   macro avg       0.55      0.54      0.54       401
weighted avg       0.59      0.61      0.59       401
```

```
Random Forest
              precision    recall  f1-score   support

           0       0.71      0.93      0.81       262
           1       0.68      0.29      0.41       139

    accuracy                           0.71       401
   macro avg       0.70      0.61      0.61       401
weighted avg       0.70      0.71      0.67       401
```

```
Neural Net
              precision    recall  f1-score   support

           0       0.72      0.87      0.79       262
           1       0.60      0.35      0.44       139

    accuracy                           0.69       401
   macro avg       0.66      0.61      0.62       401
weighted avg       0.68      0.69      0.67       401
```

```
AdaBoost
              precision    recall  f1-score   support

           0       0.70      0.95      0.80       262
           1       0.70      0.23      0.35       139

    accuracy                           0.70       401
   macro avg       0.70      0.59      0.57       401
weighted avg       0.70      0.70      0.65       401
```

```
QDA
              precision    recall  f1-score   support

           0       0.76      0.75      0.76       262
           1       0.54      0.56      0.55       139

    accuracy                           0.68       401
   macro avg       0.65      0.65      0.65       401
weighted avg       0.69      0.68      0.68       401
```

### Open-AI base-models

_(source, title, description)_

| model | accuracy | precision | recall   | auroc    | auprc    | f1       |
|-------|----------|-----------|----------|----------|----------|----------|
| ada   | 0.704545 | 0.724299  | 0.890805 | 0.742656 | 0.843987 | 0.798969 |

### BERT-base-cased

```
MODEL_NAME = 'bert-base-cased'
NUM_LABELS = 2

NUM_EPOCHS = 1
BATCH_SIZE = 32
MAX_SEQ_LEN = 512
LEARNING_RATE = 2e-5
MAX_GRAD_NORM = 1000
```

| model           | accuracy | precision | recall | auroc  | auprc  | f1     |
|-----------------|----------|-----------|--------|--------|--------|--------|
| BERT-base-cased | 0.6622   | 0.4385    | 0.6622 | 0.5000 | 0.3377 | 0.5276 |


### Collect cookies

1. Get a browser that looks like Microsoft Edge.

- a) (Easy) Install the latest version of Microsoft Edge
- b) (Advanced) Alternatively, you can use any browser and set the user-agent to look like you're using Edge (e.g., `Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.51`). You can do this easily with an extension like "User-Agent Switcher and Manager" for [Chrome](https://chrome.google.com/webstore/detail/user-agent-switcher-and-m/bhchdcejhohfmigjafbampogmaanbfkg) and [Firefox](https://addons.mozilla.org/en-US/firefox/addon/user-agent-string-switcher/).

2. Open [bing.com/chat](https://bing.com/chat)
3. If you see a chat feature, you are good to continue...
4. Install the cookie editor extension for [Chrome](https://chrome.google.com/webstore/detail/cookie-editor/hlkenndednhfkekhgcdicdfddnkalmdm) or [Firefox](https://addons.mozilla.org/en-US/firefox/addon/cookie-editor/)
5. Go to [bing.com](https://bing.com)
6. Open the extension
7. Click "Export" on the bottom right, then "Export as JSON" (This saves your cookies to clipboard)
8. Paste your cookies into a file `bing_cookies_main.json`.

[//]: # (   - NOTE: The **cookies file name MUST follow the regex pattern `bing_cookies_*.json`**, so that they could be recognized by internal cookie processing mechanisms)
