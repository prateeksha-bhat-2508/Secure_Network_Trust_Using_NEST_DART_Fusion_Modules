import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


class Visualizer:

    def __init__(self, df):

        self.df = df.copy()

    # ----------------------------------------------------
    # Hybrid Trust
    # ----------------------------------------------------

    def hybrid_trust(self):

        fig = px.bar(

            self.df.sort_values("Hybrid_Trust", ascending=False),

            x="Node_ID",

            y="Hybrid_Trust",

            color="Hybrid_Trust",

            template="plotly_dark",

            title="Hybrid Trust Score"

        )

        fig.update_layout(height=420)

        return fig

    # ----------------------------------------------------
    # Trust Evidence
    # ----------------------------------------------------

    def evidence(self):

        fig = px.bar(

            self.df,

            x="Node_ID",

            y="Unified_Trust_Evidence",

            color="Unified_Trust_Evidence",

            template="plotly_dark",

            title="Unified Trust Evidence"

        )

        fig.update_layout(height=420)

        return fig

    # ----------------------------------------------------
    # BARM
    # ----------------------------------------------------

    def barm(self):

        fig = px.bar(

            self.df,

            x="Node_ID",

            y="BARM_Score",

            color="BARM_Score",

            template="plotly_dark",

            title="BARM Score"

        )

        fig.update_layout(height=420)

        return fig

    # ----------------------------------------------------
    # ADRS
    # ----------------------------------------------------

    def adrs(self):

        fig = px.bar(

            self.df,

            x="Node_ID",

            y="ADRS_MPIQ_Score",

            color="ADRS_MPIQ_Score",

            template="plotly_dark",

            title="AdRS-MPIQ Score"

        )

        fig.update_layout(height=420)

        return fig

    # ----------------------------------------------------
    # Trust Distribution
    # ----------------------------------------------------

    def distribution(self):

        fig = px.histogram(

            self.df,

            x="Trust_Value",

            nbins=20,

            template="plotly_dark",

            title="Trust Distribution"

        )

        return fig

    # ----------------------------------------------------
    # Comparison Radar
    # ----------------------------------------------------

    def radar(self):

        row = self.df.iloc[0]

        fig = go.Figure()

        fig.add_trace(

            go.Scatterpolar(

                r=[

                    row["Hybrid_Trust"],

                    row["Unified_Trust_Evidence"],

                    row["BARM_Score"],

                    row["ADRS_MPIQ_Score"],

                    row["Trust_Value"]

                ],

                theta=[

                    "Hybrid",

                    "TEFL",

                    "BARM",

                    "AdRS",

                    "Trust"

                ],

                fill="toself",

                name=row["Node_ID"]

            )

        )

        fig.update_layout(

            template="plotly_dark",

            polar=dict(

                radialaxis=dict(

                    visible=True,

                    range=[0,1]

                )

            ),

            height=500,

            title="Trust Comparison Radar"

        )

        return fig

    # ----------------------------------------------------
    # Metrics Table
    # ----------------------------------------------------

    def metrics_table(self, metrics_df):

        import plotly.graph_objects as go

        fig = go.Figure(
            data=[
                go.Table(
                    header=dict(
                        values=[
                            "<b>Metric</b>",
                            "<b>Value</b>"
                        ],
                        fill_color="#303030",
                        font=dict(color="white", size=14),
                        align="center"
                    ),
                    cells=dict(
                        values=[
                            metrics_df["Metric"],
                            metrics_df["Proposed"].round(2)
                        ],
                        fill_color="#1f2430",
                        font=dict(color="white", size=13),
                        align="center"
                    )
                )
            ]
        )

        fig.update_layout(
            template="plotly_dark",
            height=420,
            margin=dict(l=10, r=10, t=20, b=10)
        )

        return fig

    # ----------------------------------------------------
    # Top Trusted Nodes
    # ----------------------------------------------------

    def top_nodes(self):

        return self.df.nlargest(

            10,

            "Trust_Value"

        )[

            [

                "Node_ID",

                "Trust_Value",

                "BARM_Score",

                "ADRS_MPIQ_Score"

            ]

        ]

    # ----------------------------------------------------
    # Risk Nodes
    # ----------------------------------------------------

    def risky_nodes(self):

        return self.df.nlargest(

            10,

            "Attack_Probability"

        )[

            [

                "Node_ID",

                "Attack_Probability",

                "Trust_Value"

            ]

        ]