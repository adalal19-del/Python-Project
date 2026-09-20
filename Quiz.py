import streamlit as st

st.write('Hello, I am Atul, Welcome to my Quiz Zone. Hope You like the game. you may please proceed further for my gaming.')
st.text('Q1. What is the first alphabet of English? \na.B    b.Y\nc.A    d.E\n')
ans1 = st.text_input("enter your choice for Q1....")
st.text('Q2. Who is the National Animal of India? \na.Bear    b.Giraffe  \nc.Lion    d.Tiger\n')
ans2 = st.text_input("enter your choice for Q2....")
st.text('Q3. Who is the National Bird of INdia? \na.Peacock    b.Nightingale   \nc.Hen        d.Crow\n')
ans3 = st.text_input("enter your choice for Q3....")
st.text('Q4. How many continents are there in world? \na.4    b.12   \nc.7    d.9\n')
ans4 = st.text_input("enter your choice for Q4....")
st.text('Q5. What is the capital of india? \na.Delhi    b.Mumbai  \nc.Kolkata  d.Chennai\n')
ans5=st.text_input('Enter your choice for Q5...')
st.text('Q6. Who is the Prime Minister of India? \na.Narendra Modi  b.Rahul Gandhi  \nc.Amit Shah      d.Yogi Adityanath\n')
ans6=st.text_input('Enter your choice for Q6...')
st.text('Q7. What was the old name of Mumbai?\na.Delhi  b.Maharashtra\nc.Kota  d.Bombay\n')
ans7=st.text_input('Enter Your choice for Q7...')
st.text('Q8. Who wrote the national anthem?\na Mahatma Gandhi b.Lata Mangeshkar.  \nc.Ravindranath Tagore  d. Kishore Kumar\n')
ans8=st.text_input('Enter Your choice for Q8...')
st.text('Q9. What is the capital of India?\na.Delhi b. Mumbai  \nc.Gujarat  d. New Delhi')
ans9=st.text_input('Enter your choice for Q9...')
st.text('Q10. Which is the highest mountain the world?\na.Nile Everest b.Mount Everest  \n.c Kent Everest  d. North Everest')
ans10=st.text_input('Enter your choice for Q10...')

score=0
if ans1 == 'c':
  score+=5
else:
  score-=2
st.text('Score +5')
st.text('Score -2')
if ans2=='d':
  score+=5
else:
  score-=2
st.text('Score +5')
st.text('Score -2')
if ans3=='A':
  score+=5
else:
  score-=2
st.text('Score is +5')
st.text('Score is -2')
if ans4=='c':
  score+=5
else:
  score-=2
st.text('Score is +5')
st.text('Score is -2')
if ans5=='a':
  score +=5
else:
  score-=2
st.text('Score is +5')
st.text('Score is -2')
if ans6=='a':
  score+=5
else:
  score-=2
st.text('Score is +5')
st.text('Score is -2')
if ans7=='d':
  score+=5
else:
  score-=2
st.text('Score is +5')
st.text('Score is -2')
if ans8=='c':
  score+=5
else:
  score-=2
st.text('Score is +5')
st.text('Score is -5')
if ans9=='d':
  score+=5
else:
  score-=2
st.text('Score is +5')
st.text('Score is -2')
if ans10=='b':
  score+=5
else:
  score-=2
st.text('Score is +5')
st.text('Score is -2')

st.number('Total Marks:', score)
