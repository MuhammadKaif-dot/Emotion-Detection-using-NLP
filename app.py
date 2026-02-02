import streamlit as st
import joblib

model = joblib.load("emotion_model.pkl")
vectorizer = joblib.load("bow_vectorizer.pkl")

st.title("Emotion Detection from Text")
user_input = st.text_area("Enter a sentence:", "")

emotions = {
    0: 'sadness',
    1: 'anger',
    2: 'love',
    3: 'surprise',
    4: 'fear',
    5: 'joy'
}

if st.button("Predict Emotion"):
    if user_input.strip() == "":
        st.warning("Please enter a sentence!")
    else:
        input_vec = vectorizer.transform([user_input])
        prediction_num = model.predict(input_vec)[0]
        prediction_emotion = emotions[prediction_num]
        st.success(f"Predicted Emotion: {prediction_emotion}")
