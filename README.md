# Emotion Detection using NLP

This project focuses on detecting human emotions from text using Natural Language Processing (NLP). Given a single-line sentence, the model predicts the underlying emotion expressed in the text.

The system is trained on an emotions dataset and classifies text into six emotional categories using a machine learning approach. A Streamlit web application is also developed to interactively test the model with custom inputs.

## Emotions Covered
- Sadness
- Anger
- Love
- Surprise
- Fear
- Joy

## Approach
- Text preprocessing and feature extraction using Bag-of-Words (unigrams + bigrams)
- Emotion encoding for model training
- Classification using Logistic Regression
- Model evaluation using accuracy score
- Deployment using Streamlit for real-time emotion prediction

## Tools & Technologies
- Python
- Pandas, NumPy
- Scikit-learn
- NLTK
- Streamlit
- Joblib

## Use Case
This project can be useful for:
- Emotion-aware chatbots
- Social media sentiment monitoring
- Mental health text analysis
- Customer feedback understanding

## Output
The application takes a sentence as input and predicts the corresponding emotion label.

