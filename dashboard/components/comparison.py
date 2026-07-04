import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def show(metrics_df, df):
    # =====================================================
    # PAGE TITLE
    # =====================================================
    st.title("NEST vs DART vs FUSION")
    st.markdown(
        """
        Comparative evaluation of the proposed **Trust Evidence Fusion Layer (TEFL)**,
        integrated with **Hybrid Trust**, **NEST** (Network Evidence & Structural Trust),
        **DART** (Dynamic Adaptive Risk Trust), and **Proof of Trust**
        under identical experimental conditions.
        """
    )

    st.divider()

    # =====================================================
    # CLASSIFICATION PERFORMANCE
    # =====================================================
    st.subheader("📊 Classification Performance Comparison")

    # metrics_df has columns: Metric, BARM, AdRS-MPIQ, Proposed
    # We rename them for display, but keep the underlying data unchanged.
    display_metrics = metrics_df.copy()
    display_metrics.columns = ["Metric", "NEST", "DART", "FUSION"]

    # Format numbers to 4 decimals
    styled = display_metrics.style.format({
        "NEST": "{:.4f}",
        "DART": "{:.4f}",
        "FUSION": "{:.4f}"
    })

    st.dataframe(
        styled,
        use_container_width=True,
        hide_index=True
    )

    st.divider()

    # =====================================================
    # TRUST SCORE COMPARISON
    # =====================================================
    st.subheader("🏆 Trust Score Comparison")

    # Build summary using the original column names, but label them with NEST/DART/FUSION
    summary = pd.DataFrame({
        "Framework": ["NEST", "DART", "FUSION"],
        "Average Trust": [
            df["BARM_Score"].mean(),
            df["ADRS_MPIQ_Score"].mean(),
            df["Trust_Value"].mean()
        ],
        "Maximum Trust": [
            df["BARM_Score"].max(),
            df["ADRS_MPIQ_Score"].max(),
            df["Trust_Value"].max()
        ],
        "Minimum Trust": [
            df["BARM_Score"].min(),
            df["ADRS_MPIQ_Score"].min(),
            df["Trust_Value"].min()
        ]
    })

    st.dataframe(
        summary.style.format({
            "Average Trust": "{:.4f}",
            "Maximum Trust": "{:.4f}",
            "Minimum Trust": "{:.4f}"
        }),
        use_container_width=True
    )

    # =====================================================
    # BAR CHART
    # =====================================================
    fig = px.bar(
        summary,
        x="Framework",
        y="Average Trust",
        color="Framework",
        text="Average Trust",
        title="Average Trust Score Comparison"
    )
    fig.update_traces(
        texttemplate="%{text:.4f}",
        textposition="outside"
    )
    fig.update_layout(
        template="plotly_dark",
        height=500,
        xaxis_title="Framework",
        yaxis_title="Average Trust Score",
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # =====================================================
    # RADAR CHART
    # =====================================================
    st.subheader("🎯 Trust Score Radar")
    fig = go.Figure()
    fig.add_trace(
        go.Scatterpolar(
            r=summary["Average Trust"],
            theta=summary["Framework"],
            fill="toself",
            name="Average Trust"
        )
    )
    fig.update_layout(
        template="plotly_dark",
        height=550,
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 1]
            )
        ),
        showlegend=False
    )
    st.plotly_chart(fig, use_container_width=True)

    st.divider()

    # =====================================================
    # KEY OBSERVATIONS
    # =====================================================
    st.subheader("📝 Key Observations")
    st.success(
        """
### Proposed Framework

✔ Trust Evidence Fusion Layer (TEFL)

✔ Hybrid Trust Computation

✔ NEST Integration (Network Evidence & Structural Trust)

✔ DART Optimization (Dynamic Adaptive Risk Trust)

✔ Proof of Trust Blockchain Validation

The proposed framework combines trust estimation,
routing optimization, trust evidence fusion,
and blockchain-based validation into a unified
secure IoT trust evaluation architecture.

Although the classification performance is similar
across the evaluated methods on this dataset,
the proposed framework provides richer trust estimation
through evidence fusion and improved trust scoring.
"""
    )