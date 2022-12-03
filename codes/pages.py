import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st
import numpy as np

# Setting general format to the graphs
sns.set_theme(style="white", font="sans-serif")
st.set_page_config (layout="wide")



class Pages:
    
    # Page 1 - "The Project"
    def page_one():
    # Write the title and the subheader
        st.title(
            "Breaking Zack Tabudlo into the US!"
        )
        st.subheader(
            'by Group Mic :microphone: | DSFC10'
            )
        st.markdown('Div | Sofia | JA | Pim | Andres | R | Mentor: Mike')

        col1, col2 = st.columns(2)

        with col1:
            st.image("page1col1.jpg")

        with col2:
            st.title('Harnessing data to help Zack Tabudlo make big hits in US Charts.')
            st.subheader('Empowering OPM artists into the global stage.')

        col1, col2 = st.columns(2)

        with col1:
            st.markdown("### Check out his latest release here!")
            st.video("https://www.youtube.com/watch?v=i_G6wewjOuY", format="video", start_time=0)

        with col2:
            st.image("page1col2.png")


        

    # Page 2 - "Big News for Zack!
    def page_two():
        # Write the title
        st.title(
            "Big News for Zack and other OPM Artists!"
        )
        st.image("page2pic1.png")
        st.caption(
            "Republic Records, the same record label with Ariana Grande, Drake, \
            Taylor Swift, John Legend, and many other major names in the US Music industry, launches in the Philippines \
            to **bring Filipino artists to the U.S.**")
