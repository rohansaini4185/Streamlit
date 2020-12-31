# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 12:24:17 2020

@author: Rohan Saini
"""

import numpy as np
import pickle
import pandas as pd
import streamlit as st 

from PIL import Image


pickle_in = open("Random.pkl","rb")
classifier=pickle.load(pickle_in)

def welcome():
    return "Welcome All"

def predict_note_authentication(Gender,Age,EstimatedSalary):

    """Let's Authenticate the Banks Note 
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Gender
        in: query
        type: number
        required: true
      - name: Age
        in: query
        type: number
        required: true
      - name: EstimatedSalary
        in: query
        type: number
        required: true
    responses:
        200:
            description: The output values
        
    """
    prediction=classifier.predict([[Gender,Age,EstimatedSalary]])
    print(prediction)
    return prediction
    
def main():
    st.title("Social Network")
    html_temp = """
    <div style="background-color:blue;padding:10px;">
    <h2 style="color:white;text-align:center;">Streamlit Social ML App </h2>
    </div>
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.image("DataFolkz.png", width=700)
    Gender = st.text_input("Gender","Enter Here")
    Age = st.text_input("Age","Enter Here")
    EstimatedSalary = st.text_input("EstimatedSalary","Enter Here")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(Gender,Age,EstimatedSalary)
    st.success('The output is {}'.format(result))
    if st.button("About"):
        st.text("Lets Learn")
        st.text("Built with Streamlit")

if __name__=='__main__':
    main()
    
    
    
    