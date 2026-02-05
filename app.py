# import streamlit as st
# import pickle
# import numpy as np

# # Model load karo
# model = pickle.load(open('diabetes_model.pkl', 'rb'))

# st.title("Diabetes Prediction App")
# st.write("Apni details enter karein:")

# # Input fields banana
# glucose = st.number_input("Glucose Level", min_value=0)
# bp = st.number_input("Blood Pressure", min_value=0)  # ye input lene ke liye h
# age = st.number_input("Age", min_value=1)

# if st.button("Predict"):
#     # Input ko model ke format mein convert karna
#     features = np.array([[0, glucose, bp, 0, 0, 0.0, 0.0, age]]) # Baaki inputs 0 rakhe hain simplify karne ke liye , "model ko data hamesha list ke ander list me chahiye hota h"
#     prediction = model.predict(features) # ye model se ques pooch rha ki batao diabetes h ya nhi
    
#     if prediction[0] == 1:
#         st.error("Result: Diabetes detected.")
#     else:
#         st.success("Result: No Diabetes.")

import streamlit as st
import pickle
import numpy as np

# Model load karo (Version 2 wala)
try:
    model = pickle.load(open('diabetes_model_v2.pkl', 'rb'))
except:
    st.error("Model file nahi mili! Pehle train.py chalao.")

st.set_page_config(page_title="Diabetes Predictor Pro", layout="centered")

st.title("🏥 Diabetes Health Checker")
st.write("Niche di gayi details fill karein taaki model prediction kar sake.")

# Do columns mein inputs divide karte hain (Design ke liye)
col1, col2 = st.columns(2)

with col1:
    preg = st.number_input("Pregnancies", min_value=0, max_value=20, step=1)
    glucose = st.number_input("Glucose Level", min_value=0, max_value=300)
    bp = st.number_input("Blood Pressure", min_value=0, max_value=200)
    skin = st.number_input("Skin Thickness (mm)", min_value=0, max_value=100)

with col2:
    insulin = st.number_input("Insulin Level", min_value=0, max_value=900)
    bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0, max_value=70.0, format="%.1f")
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, format="%.3f")
    age = st.number_input("Age", min_value=1, max_value=120)

# Prediction Logic
if st.button("Check Result"):
    # Saare 8 features ko ek list mein daalna (Sequence wahi hona chahiye jo training mein tha)
    user_input = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    
    prediction = model.predict(user_input)
    prediction_proba = model.predict_proba(user_input) # Probability check karne ke liye

    st.subheader("Final Result:")
    if prediction[0] == 1:
        st.error(f"High Risk: Diabetes hone ke chances hain. (Confidence: {prediction_proba[0][1]*100:.2f}%)")
    else:
        st.success(f"Low Risk: Aap safe lag rahe hain. (Confidence: {prediction_proba[0][0]*100:.2f}%)")

st.info("Note: Ye sirf ek ML project hai, medical advice ke liye doctor se milein.")

