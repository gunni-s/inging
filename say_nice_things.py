import streamlit as st
import numpy as np
import pandas as pd
import time

from PIL import Image
from random import randint
import random

image_file = st.file_uploader(label="I have thought of not 1 but 5 nice things to say to you. So when you're ready, upload any picture of yours to initiate :",
                                 type=["png", "jpeg", "jpg"])

st.markdown("<br>", unsafe_allow_html=True)  # Add space before the file uploader


m = st.markdown("""
                
<style>
div.stButton > button:first-child {
    background-color: rgb(204, 255, 229); 
    height: 2em;
    border: none;
    border-radius: 5px;
    font-size: 16px;
    font-weight: bold;
    color: #333;
    transition: background-color 0.3s ease;
}

div.stButton > button:first-child:hover {
    background-color: rgb(153, 255, 204);
}

.stMarkdown {
    font-family: 'Arial', sans-serif;
    color: #555;
    line-height: 1.5;
}

.stTitle {
    color: #0073e6;
    font-size: 24px;
    font-weight: bold;
}
</style>""", unsafe_allow_html=True)


if image_file is not None:

            img = Image.open(image_file)
            st.image(img)

            compliments = [
                "Even if you were cloned, you'd still be one of a kind. And the better looking one. 🐶",
                "If you were a triangle, you'd be a-cute one 😉",
                "If you were a fruit, you'd be a Fine-Apple 🍍😍",
                "I honestly really like how you roll your Rrrrrr's  ",
                "Are you a beaver, because damn. 😏"
            ]

            # Use session state to keep track of the compliment index
            if 'compliment_index' not in st.session_state:
                st.session_state.compliment_index = 0

            if st.button(" Be 🧀 (cheesey) to me :) 👈"):
                if st.session_state.compliment_index < len(compliments):
                    st.subheader(compliments[st.session_state.compliment_index])
                    st.session_state.compliment_index += 1
                    compliments_left = len(compliments) - st.session_state.compliment_index
                    if compliments_left > 0:
                        st.subheader(f"{compliments_left} more left.... (hit that cheese button again bb)")
                # else:
                #     st.subheader("That's all I have for now!")
                #     st.session_state.compliment_index = 0  # Reset index after all compliments are shown

            st.markdown("###     ")

            # st.write('Whenever you think you have been flattered enough, click the button below ;)')

            st.markdown("###     ")
            if st.session_state.compliment_index == 5:  # Show button after the last compliment
                if st.button(" Okay waitttt One last thing 😏"):
                    st.subheader(' If you do visit Iceland, I promise to handle you with care. So... you should. And if you dont, Im seriously considering visiting Netherlands. Call me crazy too :) ')
                    st.markdown("<br>", unsafe_allow_html=True) 
                    st.subheader(' Oh also, I hope you like balloons and snow because.... ')
                    st.subheader("Wait for it...")  # Timer message
                    # st.spinner("Loading balloons...")  # Show a spinner for a brief moment
                    time.sleep(7)  # Wait for 2 seconds
                    st.balloons()
                    st.snow()
