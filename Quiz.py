import streamlit as st

st.write('Hello, I am Atul, Welcome to my Quiz Zone. Hope You like the game. you may please proceed further for my gaming.')
st.write('Q1. What is the first alphabet of English?\n\na.B    b.Y\n\nc.A    d.E\n')
ans1 = st.text_input("enter your choice for 1....")
st.write('Q2. Who is the National Animal of India?\n\na.Bear    b.Giraffe  \n\nc.Lion    d.Tiger\n')
ans2 = st.text_input("enter your choice for 2....")
st.write('Q3. Who is the National Bird of INdia?\n\na.Peacock    b.Nightingale   \n\nc.Hen        d.Crow\n')
ans3 = st.text_input("enter your choice for 3....")
st.write('Q4. How many continents are there in world?\n\na.4    b.12   \n\nc.7    d.9\n')
ans4 = st.text_input("enter your choice for 4....")
st.write('Q5. What is the capital of india?\n\na.Delhi    b.Mumbai  \n\nc.Kolkata  d.Chennai\n')
ans5=st.text_input('Enter your choice for 5...')
st.write('Q6. Who is the Prime Minister of India?\n\na.Narendra Modi  b.Rahul Gandhi  \n\nc.Amit Shah      d.Yogi Adityanath\n')
ans6=st.text_input('Enter your choice for 6...')
st.write('Q7. What was the old name of Mumbai?\n\na.Delhi  b.Maharashtra\n\nc.Kota  d.Bombay\n')
ans7=st.text_input('Enter Your choice for 7...')
st.write('Q8. Who wrote the national anthem?\n\na Mahatma Gandhi b.Lata Mangeshkar\n\nc.Ravindranath Tagore  d. Kishore Kumar\n')
ans8=st.text_input('Enter Your choice for 8...')
st.write('Q9. What is the capital of India?\n\na.Delhi b. Mumbai  \n\nc.Gujarat  d. New Delhi')
ans9=st.text_input('Enter your choice for 9...')
st.write('Q10. Which is the highest mountain the world?\n\na.Nile Everest b.Mount Everest  \n\nc. Kent Everest  d. North Everest')
ans10=st.text_input('Enter your choice for 10...')

score=0
if not ans1 or not ans2 or not ans3 or not ans4 or not ans5 or not ans6 or not ans7 or not ans8 or not ans9 or not ans10:
  st.warning('Please answer all question before finalizing the score')
else:
  if ans1 == 'c' or ans1=='C':
    score+=5
    st.snow()
  else:
    score-=2
  if ans2=='d' or ans2=='D':
    score+=5
    st.snow()
  else:
    score-=2
  if ans3=='a' or ans3=='A':
    score+=5
    st.snow()
  else:
    score-=2
    # st.balloons()
  if ans4=='c' or ans4=='C':
    score+=5
    st.snow()
  else:
    score-=2
    # st.balloons()
  if ans5=='a' or ans5=='A':
    score +=5
    st.snow()
  else:
    score-=2
    # st.balloons()
  if ans6=='a' or ans6=='A':
    score+=5
    st.snow()
  else:
    score-=2
    # st.balloons()
  if ans7=='d' or ans7=='D':
    score+=5
    st.snow()
  else:
    score-=2
    # st.balloons()
  if ans8=='c' or ans8=='C':
    score+=5
    st.snow()
  else:
    score-=2
    # st.balloons()
  if ans9=='d' or ans9=='D':
    score+=5
    st.snow()
  else:
    score-=2
    # st.balloons()
  if ans10=='b' or ans10=='B':
    score+=5
    st.snow()
  else:
    score-=2
    # st.balloons()
  st.write('Total Marks:', score)
  
  if score>45:
    st.write('Excellent')
    st.success('Excellent')
  elif score>=30:
    st.write('Good')
  elif score>=20:
    st.write('Average')
  else:
    st.write('Better Luck Next Time')

st.write('Quiz Completed')
