import streamlit as st
total = 0
M=[86,78,98,95,90]
for i in range (5):
  total+=M[i]
  st.write(total)
  percentage=(total/5)
  st.write(percentage)
