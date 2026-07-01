import networkx as nx
import pandas as pd
from utils.constant import *




class NetworkGraph:

    def __init__(self, flow_df, node_df):

        self.flow_df = flow_df
        self.node_df = node_df
        self.graph = nx.Graph()

        self.node_df = node_df

        self.graph = nx.Graph()

    def build_graph(self):

        print(self.flow_df.shape)

        print(self.flow_df["src_ip"].nunique())
        print(self.flow_df["dst_ip"].nunique())

        print(self.flow_df[["src_ip","dst_ip"]].head(20))

        for _, row in self.flow_df.iterrows():

            src = str(row["src_ip"]).strip()
            dst = str(row["dst_ip"]).strip()

            self.graph.add_edge(src, dst)

        print("Graph Nodes :", self.graph.number_of_nodes())
        print("Graph Edges :", self.graph.number_of_edges())

        return self.graph
    def add_centrality(self):

        degree = nx.degree_centrality(self.graph)
        between = nx.betweenness_centrality(self.graph)
        close = nx.closeness_centrality(self.graph)

        # Make Node_ID exactly match graph keys
        self.node_df["Node_ID"] = self.node_df["Node_ID"].astype(str).str.strip()

        print("\nSample Graph Nodes:")
        print(list(self.graph.nodes())[:10])

        print("\nSample Node IDs:")
        print(self.node_df["Node_ID"].head(10).tolist())

        self.node_df["Degree_Centrality"] = (
            self.node_df["Node_ID"].map(degree).fillna(0)
        )

        self.node_df["Betweenness_Centrality"] = (
            self.node_df["Node_ID"].map(between).fillna(0)
        )

        self.node_df["Closeness_Centrality"] = (
            self.node_df["Node_ID"].map(close).fillna(0)
        )

        self.node_df["Centrality_Trust"] = (

            self.node_df["Degree_Centrality"]

            + self.node_df["Betweenness_Centrality"]

            + self.node_df["Closeness_Centrality"]

        ) / 3

        return self.node_df