import numpy as np
import pandas as pd
import networkx as nx


class HybridTrust:

    def __init__(self, df: pd.DataFrame):

        self.df = df.copy()

    # ------------------------------------
    # Normalize
    # ------------------------------------

    def normalize(self, x):

        if x.max() == x.min():
            return pd.Series(np.ones(len(x)))

        return (x - x.min()) / (x.max() - x.min())

    # ------------------------------------
    # Packet Delivery Ratio
    # ------------------------------------

    def packet_metrics(self):

        self.df["PDR"] = (
            self.df["dst_pkts"] /
            (self.df["src_pkts"] + 1)
        ).clip(0, 1)

        self.df["Drop_Rate"] = 1 - self.df["PDR"]

    # ------------------------------------
    # Direct Trust
    # ------------------------------------

    def direct_trust(self):

        self.df["Direct_Trust"] = (

            0.7 * self.df["PDR"]

            - 0.3 * self.df["Drop_Rate"]

        ).clip(0,1)

    # ------------------------------------
    # Reliability Trust
    # ------------------------------------

    def reliability_trust(self):

        proto = self.normalize(self.df["proto"])

        service = self.normalize(self.df["service"])

        state = self.normalize(self.df["conn_state"])

        self.df["Reliability_Trust"] = (

            proto +

            service +

            state

        ) / 3

    # ------------------------------------
    # Network Graph
    # ------------------------------------

    def build_graph(self):

        G = nx.Graph()

        for _, row in self.df.iterrows():

            G.add_edge(

                row["src_ip"],

                row["dst_ip"]

            )

        return G