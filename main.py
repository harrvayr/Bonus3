import streamlit as st
import pickle

model = pickle.load(open("sentiment_analysis_model.sav", "rb"))

prediction = ""
user_text = ""


col1, col2 = st.columns(2,gap="small",vertical_alignment="center")

def analyze_text(user_text):
    if user_text != "":
        prediction = model.predict([user_text])[0]
        with placeholder:
            st.text(f"Sentiment is {prediction}")

with col1:
    user_text = st.text_input(label="UserTextInput",label_visibility="collapsed", placeholder="Text to analyze")
    placeholder = st.empty()
    
with col2:
    st.button("Analyze", on_click=analyze_text(user_text=user_text))