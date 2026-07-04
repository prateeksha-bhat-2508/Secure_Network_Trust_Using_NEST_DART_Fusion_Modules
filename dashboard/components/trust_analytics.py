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
    # Row 2 – These charts still use internal column names,
    # but we add custom titles to show NEST and DART.
    # --------------------------------------------------
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("📊 NEST Score Distribution")
        st.plotly_chart(
            viz.barm(),      # uses BARM_Score internally
            use_container_width=True
        )

    with col2:
        st.subheader("📊 DART Score Distribution")
        st.plotly_chart(
            viz.adrs(),      # uses ADRS_MPIQ_Score internally
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
    # Statistics – rename columns for display
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

    # Map column names for frontend display only
    display_stats = stats.copy()
    display_stats.columns = [
        "Hybrid Trust",
        "Unified Trust Evidence",
        "NEST",          # <-- BARM_Score shown as NEST
        "DART",          # <-- ADRS_MPIQ_Score shown as DART
        "FUSION"         # <-- Trust_Value shown as FUSION
    ]

    st.dataframe(
        display_stats,
        use_container_width=True
    )