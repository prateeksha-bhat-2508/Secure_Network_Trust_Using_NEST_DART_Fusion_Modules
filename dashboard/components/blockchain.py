import streamlit as st
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import hashlib


def show(blockchain):

    st.title("🔗 Proof of Trust Blockchain")

    st.success("Blockchain Verification Successful")

    # ----------------------------
    # Blockchain Graph
    # ----------------------------

    # ----------------------------
# Blockchain Graph
# ----------------------------

    G = nx.DiGraph()

    blocks = blockchain[:20]

    cols = 5          # 5 blocks per row
    spacing_x = 3
    spacing_y = 2.5

    for i, block in enumerate(blocks):

        node = str(block["node"])

        # Shorten node representation
        if "." in node:
            short_node = "..." + node.split(".")[-1]
        else:
            short_node = node[-4:]

        short_hash = block["hash"][:6]

        G.add_node(
            i,
            label=f"B{i+1}\n{short_node}\n{short_hash}"
        )

    for i in range(len(blocks)-1):
        G.add_edge(i, i+1)

    # Grid layout
    pos = {}

    for i in range(len(blocks)):

        row = i // cols
        col = i % cols

        pos[i] = (
            col * spacing_x,
            -row * spacing_y
        )

    labels = nx.get_node_attributes(G, "label")

    fig, ax = plt.subplots(figsize=(15, 9))

    nx.draw_networkx_nodes(
        G,
        pos,
        node_size=2600,
        node_color="#7ec8f5",
        edgecolors="black",
        ax=ax
    )

    nx.draw_networkx_edges(
        G,
        pos,
        arrows=True,
        arrowsize=18,
        width=2,
        edge_color="gray",
        ax=ax
    )

    nx.draw_networkx_labels(
        G,
        pos,
        labels,
        font_size=8,
        font_weight="bold",
        ax=ax
    )

    ax.set_axis_off()

    st.pyplot(fig)

    st.divider()

    st.subheader("Blockchain Explorer")

    st.dataframe(

        pd.DataFrame(blockchain),

        use_container_width=True,

        height=400

    )

    # ----------------------------
    # Merkle Tree
    # ----------------------------

    st.subheader("Merkle Tree")

    hashes=[b["hash"] for b in blocks]

    def pair(a,b):

        return hashlib.sha256(

            (a+b).encode()

        ).hexdigest()

    levels=[hashes]

    while len(levels[-1])>1:

        current=levels[-1]

        nxt=[]

        for i in range(0,len(current),2):

            if i+1<len(current):

                nxt.append(

                    pair(current[i],current[i+1])

                )

            else:

                nxt.append(current[i])

        levels.append(nxt)

    tree=nx.DiGraph()

    node=0

    mapping={}

    for l,level in enumerate(levels):

        for i,h in enumerate(level):

            mapping[(l,i)]=node

            tree.add_node(node,label=h[:6])

            node+=1

    for l in range(len(levels)-1):

        for i in range(len(levels[l])):

            tree.add_edge(

                mapping[(l,i)],

                mapping[(l+1,i//2)]

            )

    pos={}

    width=len(levels[0])

    for l,level in enumerate(levels):

        step=width/len(level)

        for i in range(len(level)):

            pos[mapping[(l,i)]]=(i*step,-l)

    labels=nx.get_node_attributes(tree,"label")

    fig,ax=plt.subplots(figsize=(12,8))

    nx.draw(

        tree,

        pos,

        labels=labels,

        node_color="lightgreen",

        node_size=1800,

        font_size=8,

        ax=ax

    )

    st.pyplot(fig)