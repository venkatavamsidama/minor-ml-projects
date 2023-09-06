"""
@author: venkata vamsi
"""

import pickle 
import streamlit as st
 

pickle_in = open("C:/Users/ragha/Downloads/model.pkl","rb")
classifier = pickle.load(pickle_in)

def predict_note_authentication(variance, skewness, curtosis, entropy):
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    print(prediction)
    return prediction

def main():
    st.title("Bank auth")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center">Streamlit Bank Auth <h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    variance = st.text_input("Variance", "Type here")
    skewness = st.text_input("Skewness", "Type here")
    curtosis = st.text_input("Curtosis", "Type here")
    entropy = st.text_input("Entropy", "Type here")
    result = ""
    if st.button("Predict"):
        result = predict_note_authentication(float(variance), float(skewness), float(curtosis), float(entropy))
        st.success('The prediction is {}'.format(result))
    if st.button("About"):
        st.text("Let's learn")
        st.text("Built with Streamlit")
  

if _name_ == '_main_':
    main()