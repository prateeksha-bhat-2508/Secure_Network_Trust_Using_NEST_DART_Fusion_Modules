import streamlit as st
import pandas as pd
from visualization import Visualizer

def show(df, metrics_df):

    viz = Visualizer(df)

    st.markdown(
        """
        <div class='main-title'>
        Secure IoT Trust Intelligence Dashboard
        </div>

        <div class='sub-title'>
        Trust Evidence Fusion Layer (TEFL) |
        NEST & DART | Proof of Trust
        </div>
        """,
        unsafe_allow_html=True
    )

    st.subheader("🏆 Trust Score Comparison")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Average NEST Score",
            f"{df['BARM_Score'].mean():.4f}"
        )

    with col2:
        st.metric(
            "Average DART Score",
            f"{df['ADRS_MPIQ_Score'].mean():.4f}"
        )

    with col3:
        st.metric(
            "Average FUSION Trust",
            f"{df['Trust_Value'].mean():.4f}"
        )

    # Bar chart
    comparison = df[["BARM_Score", "ADRS_MPIQ_Score", "Trust_Value"]].mean().reset_index()
    comparison.columns = ["Framework", "Average Trust"]
    framework_map = {"BARM_Score": "NEST", "ADRS_MPIQ_Score": "DART", "Trust_Value": "FUSION"}
    comparison["Framework"] = comparison["Framework"].map(framework_map)

    import plotly.express as px
    fig = px.bar(
        comparison,
        x="Framework",
        y="Average Trust",
        color="Framework",
        text="Average Trust"
    )
    fig.update_traces(texttemplate="%{text:.4f}", textposition="outside")
    st.plotly_chart(fig, use_container_width=True)

    # KPI Cards
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("Nodes", len(df))
    with c2:
        st.metric("Average Trust", round(df["Trust_Value"].mean(), 3))
    with c3:
        st.metric("Consensus", round(df["Consensus"].iloc[0], 3))
    with c4:
        st.metric("Blockchain", "VALID")

    st.divider()

    # Trust Charts
    left, right = st.columns(2)
    with left:
        st.plotly_chart(viz.hybrid_trust(), use_container_width=True)
    with right:
        st.plotly_chart(viz.distribution(), use_container_width=True)

    st.divider()

    # Top Nodes
    left, right = st.columns(2)
    with left:
        st.subheader("🏆 Top Trusted Nodes")
        st.dataframe(viz.top_nodes(), use_container_width=True, height=350)
    with right:
        st.subheader("⚠️ Highest Risk Nodes")
        st.dataframe(viz.risky_nodes(), use_container_width=True, height=350)

    st.divider()

    # ===================================================
    # THREE-COLUMN METRICS DISPLAY (NEW)
    # ===================================================
    st.subheader("📊 Performance Metrics Comparison")

    # Rename columns for display
    display_metrics = metrics_df.copy()
    display_metrics.columns = ["Metric", "NEST", "DART", "FUSION"]

    # Option: Use a dataframe
    st.dataframe(
        display_metrics,
        use_container_width=True,
        hide_index=True
    )

    # Alternative: use a styled table or Plotly table
    # You can keep the old plotly table if you prefer, but rename the columns there as well.