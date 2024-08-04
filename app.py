import streamlit as st
import pickle
import time

st.title("Twitter Sentiment Analysis")

# Load the model
model = pickle.load(open("twitter_sentiment2.pkl", "rb"))
tweet = st.text_input("Tweet girişi yapınız:")
submit = st.button("Analiz Et")

if submit:
    start = time.time()
    prediction = model.predict([tweet])
    end = time.time()
    st.write(f"Analiz süresi: ", round(end-start, 2), "saniye")
    print(prediction[0])
    st.write("Duygu: ", prediction[0])