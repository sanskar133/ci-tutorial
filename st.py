import streamlit as st
st.title("power calculator")
st.write("enter the number to calculates it square,cube,fifth power")
n = st.number_input("Enter an integer", value=1, step=1)
square = n**2
cube = n**3
fifth_power = n**5

st.write(f"The square of {n} is: {square}")
st.write(f"The cube of {n} is: {cube}")
st.write(f"The fifth power of {n} is: {fifth_power}")