import streamlit as st
st.write('...Student Portfolio...')
Name=st.text_input('Enter Your Name..')
RN=st.text_input('Enter Your RN..')
math=st.number_input('Enter Math Marks..')
eng=st.number_input('Enter English Marks..')
hindi=st.number_input('Enter Hindi Marks..')
science=st.number_input('Enter Science Marks..')
sst=st.number_input('Enter SST Marks..')
AI=st.number_input('Enter AI Marks..')
sum=math+eng+hindi+science+sst+AI
st.write('Total Marks:',sum)
percentage=sum/6
st.write('Total percentage:',percentage)
if percentage>=90:
  st.write('Excellent')
  st.balloons()
elif percentage>=75:
  st.write('Average')
  st.snow()
elif percentage>=50:
  st.write('Fair')
else:
  st.write('Needs more practice')
