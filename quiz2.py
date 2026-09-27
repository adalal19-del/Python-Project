import streamlit as st
st.write('....Welcome to Quiz....')
name=st.text_input('Enter Your Name...')
Q=['Q1. WHat is the first alphabet of English?','Q2. Who is theNational Animal of INdia?','Q3. Who is the National Bird of India?','Q4. HOw many COntinents are there in world?']
Options=['a.B    b.Y\nc.a    d.E','a.Bear   b.Giraffe\nc.Lion   d.Tiger','a.Peacock   b.Nightingale\nc.Hen     d.Crow','a.4    b.12\nc.7    d.9']
Correct_Answer=['c','d','a','c']
user_answer=[]
score=0
for i in range(len(Q)):
  st.write(Q[i])
  st.write(Options[i])
  ans=st.text_input('Enter your choice...',key=[i]).lower()
  user_answer.append(ans)
  if Correct_Answer[i]==ans:
    score+=5
    st.snow()
  else:
    score-=2
if score ==20:
  st.write('Excellent')
  st.balloons()
elif score>15:
  st.write('Average')
  st.snow()
elif score>10:
  st.write('Poor')
else:
  st.write('Better Luck Next Time')
st.write('Name:',name)
st.write('Your Total Score:',score)
st.write('\nQuiz Completed\n')
st.write('\nThank you for your participation in the quiz contest\n')
