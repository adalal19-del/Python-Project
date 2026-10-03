import streamlit as st

st.write('Welcome to the Cricket Team Selection')

mensteam = []
womensteam = []

for i in range (5):
    name = st.text_input('Enter Your Name..')
    age = st.number_input('Enter Your Age..')
    if age >= 18:    
        gender = st.text_input('Enter Your Gender..').lower()
        st.success('Eligible')
        if gender == 'male':
            mensteam.append(name[i])
        else:
            womensteam.append(name[i])
else:
    st.warning('Not Eligible')

st.write('Men Team:', mensteam)
st.write('Women Team:', womensteam)
