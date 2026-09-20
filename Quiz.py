import streamlit as st

st.write('Hello, I am Atul, Welcome to my Quiz Zone. Hope You like the game. you may please proceed further for my gaming.')
age=st.number_input('Enter your age..')
if age >=18 and age<=58:
  st.write('You are eligible for license..')
  # st.balloons()
st.snow()
else:
  st.write('You are not eligible')
