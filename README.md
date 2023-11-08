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