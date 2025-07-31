import streamlit as st
import pandas as pd
import pickle

model1=pickle.load(open("InsurancePrediction.pkl","rb"))

def mydeploy():
    st.title("Insurance Bought Prediction")
    age=st.number_input("Enter The Age Of Customer", min_value=0, max_value=120, step=1)
    pred=st.button("Predict")

    if pred:
        df = pd.DataFrame({"age": [age]})
        x = model1.predict(df)
        if x[0] == 0:
            st.write("Not Bought Insurance")
        else:
            st.write("Bought Insurance")


mydeploy()