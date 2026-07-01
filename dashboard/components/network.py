import streamlit as st
import plotly.graph_objects as go
import numpy as np


def show(df):

    st.title("🌐 IoT Network Topology")

    st.markdown(
        """
        Color indicates **Trust Value** while marker size represents
        **Centrality Trust**. Hover over a node for detailed information.
        """
    )

    # ---------------------------------------------------
    # Generate IoT-style topology coordinates
    # ---------------------------------------------------

    n = len(df)

    cols = 8
    spacing_x = 1.8
    spacing_y = 1.6

    x = []
    y = []

    for i in range(n):

        row = i // cols
        col = i % cols

        offset = 0.9 if row % 2 else 0

        x.append(col * spacing_x + offset)
        y.append(-row * spacing_y)

    # ---------------------------------------------------
    # Gateway
    # ---------------------------------------------------

    gateway_x = (cols - 1) * spacing_x / 2
    gateway_y = 1.5

    fig = go.Figure()

    # Connection lines
    for xi, yi in zip(x, y):

        fig.add_trace(

            go.Scatter(

                x=[gateway_x, xi],
                y=[gateway_y, yi],

                mode="lines",

                line=dict(
                    color="rgba(180,180,180,0.25)",
                    width=1
                ),

                hoverinfo="skip",

                showlegend=False

            )

        )

    # ---------------------------------------------------
    # IoT Nodes
    # ---------------------------------------------------

    fig.add_trace(

        go.Scatter(

            x=x,
            y=y,

            mode="markers+text",

            text=[f"N{i+1}" for i in range(n)],

            textposition="bottom center",

            marker=dict(

                size=18 + df["Centrality_Trust"] * 60,

                color=df["Trust_Value"],

                colorscale="Viridis",

                colorbar=dict(title="Trust"),

                line=dict(color="white", width=1)

            ),

            customdata=np.stack(

                (

                    df["Node_ID"],

                    df["Trust_Value"],

                    df["Hybrid_Trust"],

                    df["Centrality_Trust"]

                ),

                axis=-1

            ),

            hovertemplate=

            "<b>%{customdata[0]}</b><br>" +

            "Trust : %{customdata[1]:.3f}<br>" +

            "Hybrid : %{customdata[2]:.3f}<br>" +

            "Centrality : %{customdata[3]:.3f}<extra></extra>",

            name="IoT Nodes"

        )

    )

    # ---------------------------------------------------
    # Gateway
    # ---------------------------------------------------

    fig.add_trace(

        go.Scatter(

            x=[gateway_x],

            y=[gateway_y],

            mode="markers+text",

            text=["Gateway"],

            textposition="top center",

            marker=dict(

                size=40,

                color="red",

                symbol="diamond"

            ),

            name="Gateway"

        )

    )

    fig.update_layout(

        template="plotly_dark",

        height=700,

        title="IoT Trust Topology",

        showlegend=False,

        xaxis=dict(

            visible=False

        ),

        yaxis=dict(

            visible=False

        ),

        margin=dict(

            l=20,
            r=20,
            t=60,
            b=20

        )

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

    st.divider()

    st.subheader("📊 Node Statistics")

    st.dataframe(

        df[
            [
                "Node_ID",
                "Centrality_Trust",
                "Hybrid_Trust",
                "Trust_Value"
            ]
        ].round(4),

        use_container_width=True

    )