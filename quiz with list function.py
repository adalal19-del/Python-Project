import streamlit as st
st.write('============================')
st.write('||....Welcome to Quiz....||')
st.write('===========================')
Q=['Q1. WHat is the first alphabet of English?','Q2. Who is theNational Animal of INdia?','Q3. Who is the National Bird of India?','Q4. HOw many COntinents are there in world?']
Options=['a. B b.Y c.A d.E',
         'a.Bear b.Giraffe c.Lion d.Tiger',
         'a.Peacock b.Nightingale c.Hen  d.Crow',
         'a.4  b.12 c.7 d.9']
Correct_Answer=['c','d','a','c']
user_answer=[]
score=0
Ques_Num=0
st.sidebar.markdown('Quiz menu...')
choice = st.sidebar.button('reset')
if choice == 0:
         for i in range (len(Q)):
                  st.write(Q[i])
                  st.write(Options[i])
                  ans=st.text_input('Enter your choice...', key = 'question_,'1).lower()
                  user_answer.append(ans)
                  st.write('===================')
                  if ans==Correct_Answer[i]:
                           score+=5
                  else:
                           score=score
                  Ques_Num+=1
         if score ==5:
                  st.write('You have won the contest')
                  st.balloons()         
         st.write(user_answer)
         st.write('Total Score:',score)
         if score==20:
                  st.write('You have done an excellent job')
                  st.balloons()
         elif score>=10:
                  st.write('Better Luck Next Time')
else:
         st.write(user_answer)
         user_answer.clear()
         score=0
         st.write('\nQuiz Completed\n')
         st.write('\nThank you for participate in the quiz contest\n') 
