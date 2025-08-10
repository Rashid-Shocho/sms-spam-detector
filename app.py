import streamlit as st
import pickle

# Load model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Streamlit UI
st.title("SMS Spam Detector")

user_input = st.text_area("Enter your SMS:")

if st.button("Predict"):
    # Transform input
    input_vec = vectorizer.transform([user_input])
    
  
    prediction = model.predict(input_vec)[0]  
  
    label_map = {0: "Ham", 1: "Spam"}
    result = label_map[prediction]
    
    st.write(f"Prediction: **{result}**")
