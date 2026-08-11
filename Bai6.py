import streamlit as st
import time
st.title("Order food")
food1 = st.text_input("What do you want to eat?")
drink1= st.text_input("What do you want to drink?")

if st.button("comfirm order"):
    st.write("your oder: ")
    st.write("food: ",food1)
    st.write("drink: ",drink1)

st.title("my progess bar: ")
myBar = st.progress(0)

for percentComplete in range(100):
    time.sleep(0.05)
    myBar.progress(percentComplete+1)

st.balloons()
st.write("thay phat sieu dep zai")