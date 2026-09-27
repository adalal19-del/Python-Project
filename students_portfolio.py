import streamlit as st
st.write('...Student Portfolio...')
Name=st.write_input('Enter Your Name..')
RN=st.write_input('Enter Your RN..')
math=st.number_input(Enter Your Marks..)
eng=st.number_input(Enter Your Marks..)
hindi=st.number_input(Enter Your Marks..)
science=st.number_input(Enter Your Marks..)
sst=st.number_input(Enter Your Marks..)
AI=st.number_input(Enter Your Marks..)
sum=math+eng+hindi+science+sst+AI
st.write('Total Marks:',sum)
percentage=sum/6
st.write('Total percentage:',percentage)
