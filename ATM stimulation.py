import streamlit as st
st.write('ATM Stimulation')
bal=15000
FD_RD=100000
name=[]
st.write("...\nWelcome To The Bank ATM\n...")
st.write('\nSaving Bank Account\nFD_RD\n')
in1=st.text_input('Enter Your Choice..')
if in1=="1":
  st.write('Welcome to Saving Bank Account')
  name=st.text_input('Enter Your Name...')
  pin=st.number_input('Enter Your Pin...')
  if (name=='Jitendra' or name=='Rohit') or pin==pin:
      st.write('Welcome to Saving Account, please select your choice below')
      st.write('1. Bank Balance\n2.Withdrawal\n3.Deposit\4.Exit')
      in2=st.text_input('Enter Your Choice...')
  if in2=='1':
    st.write('Your balance account',bal)
  elif in2=='2':
    amt=st.number_input('Please mention amount to withdrawal...')
    bal=bal-amt
    st.write('You have successfully withdraw:', amt)
    st.write('Your remaining balance:',bal)
  elif in2=='3':
    amt=st.number_input('Please mention amount to deposite...')
    bal+=amt
    st.write('You have successfully deposited the amount:',amt)
    st.write('Your overall balance:', bal)
  elif in2=='4':
    st.write('Thank you for banking with us, you have a nice day')
  else:
    st.write('Invalid choice')
else:
  st.write('Invalid Entry')
  

