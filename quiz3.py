import streamlit as st

st.write('Welcome to the Cricket Team Selection')

mensteam = []
womensteam = []
gender = st.text_input('Enter Your Gender..').lower()
if gender == 'male':
        for i in range (10):
                name = st.text_input('Enter Your Name..', key=i+10)
                age = st.number_input('Enter Your Age..', key=i+11)
                if age >= 18:
                        st.success('Eligible')
                        mensteam.append(name)
                else:
                        st.warning('Not Eligible')
elif gender=='female':
        for i in range (10):
                name = st.text_input('Enter Your Name..', key=i+12)
                age = st.number_input('Enter Your Age..', key=i+15)
                if age >= 18:
                        st.success('Eligible')
                        womensteam.append(name)
                else:
                        st.warning('Not Eligibile')
else:
    st.warning('Incorrect Input')
st.write('Men Team:', mensteam)
st.write('Women Team:', womensteam)
