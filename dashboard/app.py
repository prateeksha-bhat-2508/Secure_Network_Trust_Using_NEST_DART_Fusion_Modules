import streamlit as st
import pandas as pd
import json
from pathlib import Path
from dashboard.components.ml_intrusion import show as ml_intrusion

from styles import load_css

from dashboard.components.overview import show as overview
from dashboard.components.trust_analytics import show as analytics
from dashboard.components.tefl import show as tefl
from dashboard.components.comparison import show as comparison
from dashboard.components.blockchain import show as blockchain
from dashboard.components.network import show as network


# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Secure IoT Trust Intelligence",
    layout="wide",
    initial_sidebar_state="expanded"
)

load_css()


# =====================================================
# LOAD DATA
# =====================================================

BASE_DIR = Path(__file__).resolve().parent.parent

RESULTS_DIR = BASE_DIR / "results"

df = pd.read_csv(RESULTS_DIR / "final_results.csv")

metrics = pd.read_csv(RESULTS_DIR / "metrics.csv")

with open(RESULTS_DIR / "blockchain.json", "r") as f:
    chain = json.load(f)


# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "",
    [
        "Overview",
        "Trust Analytics",
        "Trust Evidence Fusion",
        "Comparison",
        "Blockchain",
        "Network",
        "ML Intrusion Detection"
    ]
)


# =====================================================
# ROUTING
# =====================================================

if page == "Overview":

    overview(df, metrics)

elif page == "Trust Analytics":

    analytics(df)

elif page == "Trust Evidence Fusion":

    tefl(df)

elif page == "Comparison":

    comparison(metrics, df)

elif page == "Blockchain":

    blockchain(chain)

elif page == "Network":

    network(df)

elif page == "ML Intrusion Detection":

    ml_intrusion()