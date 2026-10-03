import streamlit as st

st.write('Welcome to the Cricket Team Selection')

mensteam = []
womensteam = []
gender = st.text_input('Enter Your Gender..').lower()
st.write('Mens Team')
for i in range (11):
        name = st.text_input('Enter Your Name..', key=i)
        age = st.number_input('Enter Your Age..', key=i+11)
        if age >= 18:
                st.success('Eligible')
                mensteam.append([name, age, 'Male'])
        else:
                st.warning('Not Eligible')
st.write('Female Team')
for i in range (11):
        name = st.text_input('Enter Your Name..', key=i+22)
        age = st.number_input('Enter Your Age..', key=i+33)
        if age >= 18:
                st.success('Eligible')
                womensteam.append([name, age, 'Female'])
        else:
                st.warning('Not Eligibile')
else:
    st.warning('Incorrect Input')
st.write('Men Team:', mensteam)
st.write('Women Team:', womensteam)
st.success('Criteria for both Male and Female completed successfully')
