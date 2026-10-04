import streamlit as st
st.write('============================')
st.write('||....Welcome to Quiz....||')
st.write('===========================')
Q=['Q1. WHat is the first alphabet of English?','Q2. Who is theNational Animal of INdia?','Q3. Who is the National Bird of India?','Q4. HOw many COntinents are there in world?']
Options=['a.B \nb.Y \nc.A \nd.E',
         'a.Bear  \nb.Giraffe \nc.Lion   \nd.Tiger',
         'a.Peacock   \nb.Nightingale \nc.Hen     \nd.Crow',
         'a.4    \nb.12 \nc.7    \nd.9']
Correct_Answer=['c','d','a','c']
user_answer=[]
score=0
Ques_Num=0
choice = st.sidebar.button('reset')
if choice == 0:
         for question in Q:
                  st.write('===================')
                  st.write(question)
                  for option in options(Ques_Num):
                           st.write(option)
                  ans=st.text_input('Enter your choice...',key = i,placeholder = 'enter to confirm').lower()
                  user_answer.append(ans)
                  if (user_answer[Ques_Num]==Correct_Answer[Ques_Num]):
                           score+=5
                  else:
                           score=score
                  Ques_Num+=1
         else:
                  if score ==5:
                           st.write('You have won the contest')
                           st.balloons()         
         st.write(user_answer)
         st.write('Total Score:',score)
else:
         st.write(user_answer)
         user_answer.clear()
         score=0
         st.write('\nQuiz Completed\n')
         st.write('\nThank you for participate in the quiz contest\n') 
