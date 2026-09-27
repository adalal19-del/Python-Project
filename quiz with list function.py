import steamlit as st
st.write('....Welcome to Quiz....')
Q=['Q1. WHat is the first alphabet of English?','Q2. Who is theNational Animal of INdia?','Q3. Who is the National Bird of India?','Q4. HOw many COntinents are there in world?']
Options=['a.B    b.Y\nc.A    d.E','a.Bear   b.Giraffe\nc.Lion   d.Tiger','a.Peacock   b.Nightingale\nc.Hen     d.Crow','a.4    b.12\nc.7    d.9']
Correct_Answer=['c','d','a','c']
user_answer=[]
score=0
for i in range(len(q)):
  st.text(Q[i])
  st.text(O[i])
  ans=st.write('Enter 
