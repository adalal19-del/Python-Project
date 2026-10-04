import streamlit as st
st.write('============================')
st.write('||....Welcome to Quiz....||')
st.write('===========================')
Q=['Q1. WHat is the first alphabet of English?','Q2. Who is theNational Animal of INdia?','Q3. Who is the National Bird of India?','Q4. HOw many COntinents are there in world?']
Options=['a.B    b.Y c.A    d.E',
         'a.Bear   b.Giraffe c.Lion   d.Tiger',
         'a.Peacock   b.Nightingale c.Hen     d.Crow',
         'a.4    b.12 c.7    d.9']
Correct_Answer=['c','d','a','c']
user_answer=[]
score=0
choice = st.sidebar.button('reset')
for i in range(len(Q)):
  st.write(Q[i])
  st.write(Options[i])
  ans=st.text_input('Enter your choice...',key = i,placeholder = 'enter to confirm').lower()
  user_answer.append(ans)
  if Correct_Answer[i]==ans:
           score+=5
           st.balloons()
  else:
           score=score
           user_answer.clear()
else:
         st.write(user_answer)
         user_answer.clear()
         score=0
         st.write('\nQuiz Completed\n')
         st.write('\nThank you for participate in the quiz contest\n') 
