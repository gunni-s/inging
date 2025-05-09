import streamlit as st
import numpy as np
import pandas as pd
import time

from PIL import Image
from random import randint
import random

image_file = st.file_uploader(label="I have some news and I couldn't find another way to break it..... So when you're ready, upload any picture of yours to initiate :",
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
                "I'm coming to see you INGER...... NOT (in borats voice)",
                "....NOT.......(get it? because i'm coming to see you... not not.... which means I am coming to see you) WAIT HOLD UP then hows this bad news? GOOD QUESTION",
                "because i'm bringing cheese, bad dad jokes, and a whole lot of annoying me to your doorstep.... such as.....",
                "If you were a dessert, you’d be the one I tell myself I’ll only have a bite of and then finish the whole thing.",
                "Are you made of copper and tellurium? Because you’re Cu-Te 😘",
                "YEP, its 'appening innit. I can't wait to fight with you in public.... (win the argument - maybe illl let you win one) and then",
                " kiss and make up and be like teehee and then share the beer and then cuddle and hug, and some more kisses ",
                
            ]

            # Use session state to keep track of the compliment index
            if 'compliment_index' not in st.session_state:
                st.session_state.compliment_index = 0

            if st.button(" Ruin me with this news 😫"):
                if st.session_state.compliment_index < len(compliments):
                    st.subheader(compliments[st.session_state.compliment_index])
                    st.session_state.compliment_index += 1
                    compliments_left = len(compliments) - st.session_state.compliment_index
                    if compliments_left > 0:
                        st.subheader(f" hit that NEWS button again bb, there's more....")
                # else:
                #     st.subheader("That's all I have for now!")
                #     st.session_state.compliment_index = 0  # Reset index after all compliments are shown

        
            # st.markdown("###     ")
            if st.session_state.compliment_index == 5:  # Show button after the last compliment
                if st.button(" all this to say 😏"):
                    st.subheader('I AM COMING TO SEE YOU MISS SUNFLOWER AND I CANNOT WAIT!!!😘 ')
                    st.markdown("<br>", unsafe_allow_html=True) 
                    st.subheader(' Oh also, I hope you STILL like balloons and snow because.... ')
                    st.subheader("Wait for it...")  # Timer message
                    # st.spinner("Loading balloons...")  # Show a spinner for a brief moment
                    time.sleep(5)  # Wait for 2 seconds
                    st.balloons()
                    st.snow()
