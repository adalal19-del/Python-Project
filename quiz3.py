import streamlit as st

st.write('Welcome to the Cricket Team Selection')

age = st.number_input('Enter Your Age..', min_value=0)

if age < 18:
    st.warning('Not Eligible')
    st.stop()

st.success('Eligible')

men_team = []
women_team = []

st.subheader('Men Team')
for i in range(5):
    name = st.text_input(f'Enter Men Team Name {i + 1}..', key=f'men_{i}')
    if name.strip():
        men_team.append(name.strip())

st.subheader('Women Team')
for i in range(5):
    name = st.text_input(f'Enter Women Team Name {i + 1}..', key=f'women_{i}')
    if name.strip():
        women_team.append(name.strip())

st.write('Mens Team:', men_team)
st.write('Womens Team:', women_team)
