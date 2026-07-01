import streamlit as st
import plotly.express as px


def show(df):

    st.title("🧠 Trust Evidence Fusion Layer (TEFL)")

    st.info(
        """
        The proposed Trust Evidence Fusion Layer (TEFL) combines
        multiple trust dimensions into a Unified Trust Evidence
        representation before BARM and AdRS-MPIQ processing.
        """
    )

    # =======================================================
    # KPIs
    # =======================================================

    c1, c2, c3 = st.columns(3)

    with c1:

        st.metric(
            "Average Evidence",
            round(df["Evidence_Vector"].mean(), 3)
        )

    with c2:

        st.metric(
            "Confidence",
            round(df["Evidence_Confidence"].mean(), 3)
        )

    with c3:

        st.metric(
            "Unified Trust",
            round(df["Unified_Trust_Evidence"].mean(), 3)
        )

    st.divider()

    # =======================================================
    # Evidence Vector
    # =======================================================

    fig = px.bar(

        df.sort_values(
            "Unified_Trust_Evidence",
            ascending=False
        ),

        x="Node_ID",

        y="Evidence_Vector",

        color="Evidence_Vector",

        template="plotly_dark",

        title="Trust Evidence Vector"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =======================================================
    # Confidence
    # =======================================================

    fig = px.bar(

        df,

        x="Node_ID",

        y="Evidence_Confidence",

        color="Evidence_Confidence",

        template="plotly_dark",

        title="Evidence Confidence"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # =======================================================
    # Unified Trust Evidence
    # =======================================================

    fig = px.bar(

        df,

        x="Node_ID",

        y="Unified_Trust_Evidence",

        color="Unified_Trust_Evidence",

        template="plotly_dark",

        title="Unified Trust Evidence"

    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.divider()

    st.subheader("TEFL Formulation")

    st.latex(r"""
    Evidence =
    0.35H +
    0.25B +
    0.15R +
    0.15Rel +
    0.10C
    """)

    st.latex(r"""
    Confidence =
    0.60Hist +
    0.40Neighbor
    """)

    st.latex(r"""
    Unified\ Trust\ Evidence=
    0.70Evidence+
    0.30Confidence
    """)