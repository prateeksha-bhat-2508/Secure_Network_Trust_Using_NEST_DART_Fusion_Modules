import streamlit as st


def load_css():

    st.markdown("""

    <style>

    .stApp{

        background:#0E1117;
        color:white;

    }

    .main-title{

        font-size:40px;

        font-weight:700;

        text-align:center;

        color:#4FC3F7;

        padding:10px;

    }

    .sub-title{

        font-size:18px;

        text-align:center;

        color:#BBBBBB;

        margin-bottom:25px;

    }

    .metric-card{

        background:#1B1F27;

        padding:20px;

        border-radius:15px;

        border:1px solid #30363d;

        box-shadow:0px 0px 10px rgba(0,255,255,0.15);

        text-align:center;

    }

    .metric-title{

        font-size:18px;

        color:#A0AEC0;

    }

    .metric-value{

        font-size:28px;

        font-weight:bold;

        color:#00E5FF;

    }

    hr{

        border:1px solid #30363d;

    }

    </style>

    """,unsafe_allow_html=True)