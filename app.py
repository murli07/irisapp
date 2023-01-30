


import streamlit as st
import pickle

model = pickle.load(open('model.pkl','rb'))

st.sidebar.header("Enter your parameter")

a = st.sidebar.slider("Sepal Length",2.0,8.0,5.5)
b = st.sidebar.slider("Sepal Width",2.0,8.0,2.5)
c = st.sidebar.slider("Petal Length",2.0,8.0,3.5)
d = st.sidebar.slider("Petal Width",2.0,8.0,1.5)

pred = model.predict([[a,b,c,d]])

st.header("Your Output ")
st.subheader(pred[0])


# In[ ]:




