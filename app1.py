
import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"


def predict_note_authentication(SESSO, AGE, WBC, Piastrine, Neutrofili, Monociti, Eosinofili, Basofili, AST, ALT, ALP, GGT, LDH):
    
    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: SESSO
        in: query
        type: number
        required: true
      - name: AGE
        in: query
        type: number
        required: true
      - name: WBC
        in: query
        type: number
        required: true
      - name: Piastrine
        in: query
        type: number
        required: true
      - name: Neutrofili
        in: query
        type: number
        required: true
      - name: Monociti
        in: query
        type: number
        required: true
      - name: Eosinofili
        in: query
        type: number
        required: true
      - name: Basofili
        in: query
        type: number
        required: true
      - name: AST
        in: query
        type: number
        required: true
      - name: ALT
        in: query
        type: number
        required: true
      - name: ALP
        in: query
        type: number
        required: true
      - name: GGT
        in: query
        type: number
        required: true
      - name: LDH
        in: query
        type: number
        required: true

    responses:
        200:
            description: The output values
        
    """
   
    prediction=classifier.predict([[SESSO, AGE, WBC, Piastrine, Neutrofili, Monociti, Eosinofili, Basofili, AST, ALT, ALP, GGT, LDH]])
    print(prediction)
    return prediction


def main():
    st.title("Covid'19")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Covid'19 </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    SESSO = st.text_input("Gender (For Male type: 0 / For Female type: 1)","Type Here")
    AGE = st.text_input("AGE","Type Here")
    WBC = st.text_input("WBC","Type Here")
    Piastrine = st.text_input("Piastrine","Type Here")
    Neutrofili = st.text_input("Neutrofili","Type Here")
    Monociti = st.text_input("Monociti","Type Here")
    Eosinofili = st.text_input("Eosinofili","Type Here")
    Basofili = st.text_input("Basofili","Type Here")
    AST = st.text_input("AST","Type Here")
    ALT = st.text_input("ALT","Type Here")
    ALP = st.text_input("ALP","Type Here")
    GGT = st.text_input("GGT","Type Here")
    LDH = st.text_input("LDH","Type Here")

    result=""
    if st.button("Predict"):
        result=predict_note_authentication(SESSO, AGE, WBC, Piastrine, Neutrofili, Monociti, Eosinofili, Basofili, AST, ALT, ALP, GGT, LDH)
    st.success('The output is  {}'.format(result))
    if st.button("About"):
        st.text("Coronavirus disease (COVID-19) is an infectious disease caused by a newly discovered coronavirus.")
        st.text("Most people who fall sick with COVID-19 will experience mild to moderate symptoms and recover without special treatment.")

if __name__=='__main__':
    main()
    
    
    
