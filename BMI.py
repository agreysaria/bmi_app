import streamlit as st
import pandas as pd


st.markdown(
    """
    <style>
    .watermark {
        position: fixed;
        bottom: 10px;
        right: 10px;
        opacity: 0.5;
        font-size: 12px;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add the watermark text
st.markdown('<p class="watermark">Designed by Agrey Saria</p>', unsafe_allow_html=True)

st.title("BMI calculator", anchor=False)
height = st.slider("Enter your height (in cm): ",100, 250, 175)
weight = st.slider("Enter your weight (in kg): ",40, 200, 75)

bmi = weight / ((height/100)**2)

st.write(f"Your BMI is {bmi:.2f}")
st.subheader("BMI Categories", anchor=False)
st.write("Underweight: Less than 18.5")
st.write("Healthy weight: 18.5 to less than 25")
st.write("Overweight: 25 to less than 30")
st.write("Obesity: 30 or greater")