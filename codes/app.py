import streamlit as st
from pages import Pages

list_of_pages = [
    "Testing 1",
    "Testing 2"
]

st.sidebar.title('Breaking into the US! :notes:')
st.sidebar.markdown('by Group Mic :microphone: | DSFC10')
st.sidebar.image("sidebarpic.jpg")
selection = st.sidebar.radio("Go to: ", list_of_pages)

if selection == "Testing 1":
    Pages.page_one()

elif selection == "Testing 2":
    Pages.page_two()
