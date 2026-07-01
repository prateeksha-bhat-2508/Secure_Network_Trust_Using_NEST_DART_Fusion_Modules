import numpy as np


class UG:

    def __init__(self, node_df):
        self.df = node_df

    def compute(self):

        self.df["UG"] = (

            0.6 * self.df["Unified_Trust_Evidence"]

            + 0.4 * self.df["Neighbor_Trust"]

        ).clip(0, 1)

        return self.df