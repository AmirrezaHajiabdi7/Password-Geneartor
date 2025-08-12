import streamlit as st
from src.passwordgeneartor import pin_password, random_password, memorable_password

st.title(":zap: PasswordGenerator Free")


option = st.radio(
    "select a password geneartor",
    ("pin code", "Memorable password", "random password")
)

if option == 'pin code':
    lenght = st.slider("select the lenght of the pin code ", 4, 12)
    password = pin_password(lenght)
    st.write(f"your password is : `{password}`")

if option == 'random password':
    lenght = st.slider("select the length of the random password", 8, 100)
    include_number = st.toggle("Include Number")
    include_symbol = st.toggle("Include Symbol")
    password = random_password(lenght, include_number, include_symbol)
    st.write(f"your password is : ``` {password} ```")

if option == 'Memorable password':
    lenght = st.slider("select the length of the random password", 4, 12)
    capitalize = st.toggle("Capitalize")
    separator = st.text_input("Separator", value="_")
    password = memorable_password(lenght, capitalize, separator)
    st.write(f"your password is : ``` {password} ```")
