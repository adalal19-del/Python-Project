import streamlit as st

name=['Jitendra','Rohit']
bal=[100000,200000]
pin=[1234,12345]
fd_rd=[200000,300000]
st.write('****Welcome to ATM Stimulation****')
st.write('\n1.Saving Account\n2.fd_rd')
choice=st.text_input('Enter your choice key..', placeholder = 'Enter 1, 2')
choice = st.sidebar.button('reset')
if choice=='1':
  st.write('Welcome to Saving Account')
  names=st.text_input('Enter Your Name ..',1)
  pins=st.number_input('Enter Your Pin..',2)
  if names in name:
    j=name.index(names)
    if pin==pins[j]:
      st.write('1. Deposit\n2.Balance in Account\n3.Withdrawal\n4.Exit')
      in2=st.write('Enter Your Choice...',3)
      if in2=='1':
          amt=st.number_input('Enter the amt to deposit..')
          bal[j]=bal[j]+amt
          st.write('Successfully Deposit Amt:',amt)
          st.write('Total balance:',bal[j])
      if in2=='2':
          st.write('Total balance:',bal[j])
      if in2=='3':
          amt1=st.number_input('Enter the amt to withdrawal...')
          bal[j]=bal[j]-amt
          st.write('Successfully withdrawal amount:',amt2)
          st.write('Total balance:',bal[j])
      if in2=='4':
          st.write('Thank you for banking with us')
      else:
        st.write('Hope you have a good day')
  else:
      st.write('Invalid input')
else:
  st.write('Invalid entry')
        
