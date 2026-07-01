import numpy as np


class Reputation:

    def __init__(self, node_df):
        self.df = node_df

    def compute(self):

        self.df["Reputation"] = (

            0.7 * self.df["RA"]

            + 0.3 * self.df["Historical_Trust"]

        ).clip(0, 1)

        return self.df