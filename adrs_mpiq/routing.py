import numpy as np


class Routing:

    def __init__(self, df):
        self.df = df

    def compute(self):

        self.df["Routing_Score"] = (

            0.6 * self.df["Hybrid_Trust"]

            + 0.4 * self.df["Centrality_Trust"]

        ).clip(0,1)

        return self.df