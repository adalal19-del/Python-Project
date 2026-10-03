import streamlit as st

st.write('Welcome to the Cricket Team Selection')

mensteam = []
womensteam = []

for i in range (5):
    name = st.number_input('Enter Your Name..', key=i)
    age = st.number_input('Enter Your Age..', key=i+5)
    gender = st.text_input('Enter Your Gender..',key=i+10).lower()
    if age >= 18:
        st.success('Eligible')
        if gender == 'male':
            mensteam.append(name[i])
        else:
            womensteam.append(name[i])
        i+=1
    else:
        st.warning('Not Eligible')

st.write('Men Team:', mensteam)
st.write('Women Team:', womensteam)
