import numpy as np


class RA:

    def __init__(self, node_df):
        self.df = node_df

    def compute(self):

        self.df["RA"] = (

            self.df["UG"]

            * self.df["Centrality_Trust"]

        ).clip(0, 1)

        return self.df