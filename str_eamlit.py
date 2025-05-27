import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.markdown(
    """
    <style>
    .big-font {
        font-size:30px !important;
        color: blue;
    }
    </style>
    """, unsafe_allow_html=True
)


title="anjali"
st.markdown(f'<p class="big-font">This is a big blue {title}!</p>', unsafe_allow_html=True)

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 10, 30, 40])
st.pyplot(fig)


df = pd.DataFrame(np.random.randn(5, 3), columns=['A', 'B', 'C'])
st.dataframe(df)

st.title("Hello, Anjali!")

st.write("Welcome to your first Streamlit app.")

st.header("Header Example")
st.subheader("Subheader Example")
st.text("This is plain text.")
st.markdown("**This is bold text using markdown.**")
st.code("x = 5", language='python')
st.latex(r'\frac{a}{b}')
##########################################################################################

# Inject custom CSS to style the output text
st.markdown("""
    <style>
    /* Pink text output */
    .pink-text {
        color: hotpink;
        font-size: 20px;
        font-weight: bold;
    }

    /* Style text input box */
    input[type="text"] {
        border: 2px solid hotpink;
        padding: 5px;
        color: hotpink;
        font-weight: bold;
    }

    /* Style slider track and thumb */
    .stSlider > div[data-baseweb="slider"] > div {
        color: hotpink;  /* affects selected range */
    }
    .stSlider .css-14pt78w {
        background-color: hotpink; /* slider thumb */
    }
    .stSlider .css-1n76uvr {
        background-color: hotpink; /* slider bar */
    }
    </style>
""", unsafe_allow_html=True)

# Input fields
name = st.text_input("Enter your name")

# Display styled output using HTML
if name:
    st.markdown(f'<p class="pink-text">Hello, {name}!</p>', unsafe_allow_html=True)

age = st.slider("Select your age", 0, 100)

# Display styled output using HTML
st.markdown(f'<p class="pink-text">Your age is: {age}</p>', unsafe_allow_html=True)


# name = st.text_input("Enter your name")
# st.write(f"Hello, {name}!")

# age = st.slider("Select your age", 0, 100)
# st.write(f"Your age is: {age}")
st.markdown("""
    <style>
        .stButton > button {
            background-color: #e83e8c;  /* Pink */
            color: white;
            border-radius: 10px;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit native button
if st.button("Click Me"):
    st.success("You clicked the button!")