import streamlit as st

from visualization import Visualizer


def show(df):

    viz = Visualizer(df)

    st.title("📊 Trust Analytics")

    st.markdown(
        "Comparison of all trust models generated in the proposed framework."
    )

    # --------------------------------------------------
    # Row 1
    # --------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.plotly_chart(
            viz.hybrid_trust(),
            use_container_width=True
        )

    with col2:

        st.plotly_chart(
            viz.evidence(),
            use_container_width=True
        )

    # --------------------------------------------------
    # Row 2
    # --------------------------------------------------

    col1, col2 = st.columns(2)

    with col1:

        st.plotly_chart(
            viz.barm(),
            use_container_width=True
        )

    with col2:

        st.plotly_chart(
            viz.adrs(),
            use_container_width=True
        )

    # --------------------------------------------------
    # Radar
    # --------------------------------------------------

    st.subheader("Trust Comparison Radar")

    st.plotly_chart(
        viz.radar(),
        use_container_width=True
    )

    # --------------------------------------------------
    # Statistics
    # --------------------------------------------------

    st.subheader("Summary Statistics")

    stats = df[
        [
            "Hybrid_Trust",
            "Unified_Trust_Evidence",
            "BARM_Score",
            "ADRS_MPIQ_Score",
            "Trust_Value"
        ]
    ].describe()

    st.dataframe(
        stats,
        use_container_width=True
    )