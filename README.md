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
