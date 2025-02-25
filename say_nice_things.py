import streamlit as st
import numpy as np
import pandas as pd

from PIL import Image
from random import randint
import random


image_file = st.file_uploader(label="Upload your picture to initiate your birthday gift",
                                 type=["png", "jpeg", "jpg"])

m = st.markdown("""
<style>
div.stButton > button:first-child {
background-color: rgb(204, 255, 229);height:3em;
}
</style>""", unsafe_allow_html=True)



if image_file is not None:

            img = Image.open(image_file)
            # img = np.array(img)
            st.image(img)

            

            def compliment():
                value = randint(2, 6)
                if value == 2:
                    st.subheader("Even if you were cloned, you'd still be one of a kind. And the better looking one. 🐶")
                elif value==3:
                    st.subheader("Mamaa miaaaa 🤌 🤌 -- *italian chef kiss* -- ")
                elif value==4:
                    st.subheader("If you were a fruit, you'd be a Fine-Apple 🍍😍")
                elif value==5:
                    st.subheader("You might be the primary reason for global warming. 🥵 🥵 ")
                else:
                    st.subheader("Are you a beaver, because damn. 😏")

                return 




            if st.button("Tell me something about myself :) 👈"):
                compliment()

            st.markdown("###     ")


            # st.write('Whenever you think you have been flattered enough, click the button below ;)')

            st.markdown("###     ")

            if st.button("One last thing 😏"):
                #     st.balloons()
                st.title(' Ta-daaaa')
                st.balloons()
