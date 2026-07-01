import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


def show(metrics_df, df):

    # =====================================================
    # PAGE TITLE
    # =====================================================

    st.title("⚖️ BARM vs AdRS-MPIQ vs Proposed Framework")

    st.markdown(
        """
        Comparative evaluation of the proposed **Trust Evidence Fusion Layer (TEFL)**,
        integrated with **Hybrid Trust**, **BARM**, **AdRS-MPIQ**, and **Proof of Trust**
        under identical experimental conditions.
        """
    )

    st.divider()

    # =====================================================
    # CLASSIFICATION PERFORMANCE
    # =====================================================

    st.subheader("📊 Classification Performance")

    performance = pd.DataFrame({

        "Metric": metrics_df["Metric"],

        "Value": metrics_df["Proposed"]

    })

    performance["Value"] = performance["Value"].map(
        lambda x: f"{x:.2f}"
    )

    st.table(performance)

    st.divider()

    # =====================================================
    # TRUST SCORE COMPARISON
    # =====================================================

    st.subheader("🏆 Trust Score Comparison")

    summary = pd.DataFrame({

        "Framework": [

            "BARM",

            "AdRS-MPIQ",

            "Proposed"

        ],

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

    st.plotly_chart(

        fig,

        use_container_width=True

    )

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

    st.plotly_chart(

        fig,

        use_container_width=True

    )

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

✔ BARM Integration

✔ AdRS-MPIQ Optimization

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