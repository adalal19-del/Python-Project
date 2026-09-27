import streamlit as st
Name=st.write('Enter Your Name..')
RN=st.write('Enter Your RN..')
math=st.number(Enter Your Marks..)
eng=st.number(Enter Your Marks..)
hindi=st.number(Enter Your Marks..)
science=st.number(Enter Your Marks..)
sst=st.number(Enter Your Marks..)
AI=st.number(Enter Your Marks..)
sum=math+eng+hindi+science+sst+AI
st.write('Total Marks:',sum)
percentage=sum/6
st.write('Total percentage:',percentage)
