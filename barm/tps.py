import numpy as np


class TPS:

    def __init__(self, node_df):
        self.df = node_df

    def compute(self):

        self.df["BARM_Score"] = (

            self.df["Updated_Trust"]

        ).clip(0, 1)

        return self.df