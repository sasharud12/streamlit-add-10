import streamlit as st

st.title("Додавання 10 до числа")

num = st.number_input("Введи число:", step=1)

if st.button("Додати 10"):
    result = num + 10
    st.success(f"Результат: {result}")