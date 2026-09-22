import streamlit as st 

a=st.number_input("enter your number")
b=st.number_input("enter another number")
if-st.button("add"):
      st.success(a+b)
elif st.button("subtract"):
      st.success(a-b)
elif st.button("multiply"):
      st.success(a*b)



