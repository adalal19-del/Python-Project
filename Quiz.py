import streamlit as st

st.write('Hello, I am Atul, Welcome to my Quiz Zone. Hope You like the game. you may please proceed further for my gaming.')
st.text('Q1. What is the first alphabet of English? \na.B    b.Y\nc.A    d.E\n')
ans1 = st.text_input("enter your choice....")
st.text('Q2. Who is the National Animal of India? \na.Bear    b.Giraffe  \nc.Lion    d.Tiger\n')
ans2 = st.text_input("enter your choice....")
st.text('Q3. Who is the National Bird of INdia? \na.Peacock    b.Nightingale   \nc.Hen        d.Crow\n')
ans3 = st.text_input("enter your choice....")
st.text('Q4. How many continents are there in world? \na.4    b.12   \nc.7    d.9\n')
ans4 = st.text_input("enter your choice....")
st.text('Q5. What is the capital of india? \na.Delhi    b.Mumbai  \nc.Kolkata  d.Chennai\n')
ans5=st.text_input('Enter your choice...')
st.text('Q6. Who is the Prime Minister of India? \na.Narendra Modi  b.Rahul Gandhi  \nc.Amit Shah      d.Yogi Adityanath\n')
ans6=st.text_input('Enter your choice...')
st.text('Q7. What was the old name of Mumbai?\na.Delhi  b.Maharashtra\nc.Kota  d.Bombay\n')
ans7=st.text_input('Enter Your choice...')
st.text('Q8. Who wrote the national anthem?\na Mahatma Gandhi b.Lata Mangeshkar.  \nc.Ravindranath Tagore  d. Kishore Kumar\n')
ans8=st.text_input('Enter Your choice...')
st.text('Q9. What is the capital of India?\na.Delhi b. Mumbai  \nc.Gujarat  d. New Delhi')
ans9=st.text_input('Enter your choice...')
st.text('Q10. Which is the highest mountain the world?\na.Nile Everest b.Mount Everest  \n.c Kent Everest  d. North Everest')
ans10=st.text_input('Enter your choice...')

score=0
if ans1 == 'c' or ans1 == 'C':
  score+=5
else:
  score-=2
st.text('Score +5')
st.text('Score -2')
if ans2=='d' or ans2!='D':
  score+=5
else:
  score-=2
st.text('Score +5')
st.text('Score -2')
if ans3=='A' or ans3!='a':
  score+=5
else:
  score-=5
st.text('Score is +5')
st.text('Score is -2')
if ans4=='c' or ans3!='A':
  score+=5
else:
  score-=4
st.text('Score is +5')
st.text('Score is -2')
if ans5=='a'or ans5!='A':
  score +=5
else:
  score-=5
st.text('Score is +5)
st.text('Score is -2')
if ans6=='a' or ans6!='A':
  score+=5
else:
  score-=5
st.text('Score is +5')
st.text('Score is -5')
if ans7=='d' or ans7!='D':
  score+=5
else:
  score-=5
st.text('Score is +5')
st.text('Score is -2')
if ans8=='c' or ans8!='C':
  score+=5
else:
  score-=5
st.text('Score is +5')
st.text('Score is -5')
if ans9=='d' or ans9!="D"
  score+=5
else:
  score-=5
st.text('Score is +5')
st.text('Score is -2')
if ans10=='b' or ans10!='D':
  score+=5
else:
  score-=2
st.text('Score is +5')
st.text('Score is -2')

st.text('Total Marks:', score)
