import numpy as np


class TrustUpdate:

    def __init__(self, node_df):
        self.df = node_df

    def compute(self):

        self.df["Updated_Trust"] = (

            0.5 * self.df["Reputation"]

            + 0.5 * self.df["Hybrid_Trust"]

        ).clip(0, 1)

        return self.df