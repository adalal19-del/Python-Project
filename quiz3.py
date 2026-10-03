st.write('Welcome to the Cricket Team Selection')

mensteam = []
womensteam = []

name = st.text_input('Enter Your Name..')
age = st.number_input('Enter Your Age..')
if age >= 18:
    for i in range (5):
    gender = st.text_input('Enter Your Gender..')
    st.success('Eligible')
    i+=gender
    if gender == 'male':
        mensteam.append(name)
    else:
        gender == 'female':
        womensteam.append(name)
else:
    st.warning('Not Eligible')

st.write('Men Team:', mensteam)
st.write('Women Team:', womensteam)
