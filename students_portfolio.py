import streamlit as st
st.write('...Student Portfolio...')
Name=st.text_input('Enter Your Name..')
RN=st.text_input('Enter Your RN..')
math=st.number_input('Enter Your Marks..',max_value=100)
eng=st.number_input('Enter Your Marks..',max_value=100)
hindi=st.number_input('Enter Your Marks..',max_value=100)
science=st.number_input('Enter Your Marks..',max_value=100)
sst=st.number_input('Enter Your Marks..',max_value=100)
AI=st.number_input('Enter Your Marks..',max_value=100)
sum=math+eng+hindi+science+sst+AI
st.write('Total Marks:',sum)
percentage=sum/6
st.write('Total percentage:',percentage)
