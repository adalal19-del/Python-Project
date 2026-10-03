import streamlit as st
st.write('Welcome to the Cricket Team Selection')
name=st.text_input('Enter Your Name..')
age=st.number_input('Enter Your Age..')
# name[]
# Gender[male, female]
mensteam=[]
womensteam=[]
for in range (0,5):
  if age>=18:
    gender=st.text_input('Enter Your Gender..').lower()
    st.success('Eligible')
    if gender == 'male':
    # j=name.index(name)
      mensteam.append(name)
    else:
      womensteam.append(name)
  else:
    st.warning('Not Eligible')
st.write('Mens Team:',mensteam)
st.write('Womens Team:', womensteam)
  
