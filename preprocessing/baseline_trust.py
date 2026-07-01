import numpy as np
import pandas as pd


class BaselineTrust:

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def normalize(self, col):

        x = self.df[col].astype(float)

        if x.max() == x.min():
            return pd.Series(np.ones(len(x)))

        return (x - x.min()) / (x.max() - x.min())

    # -----------------------------------
    # Behaviour Trust
    # -----------------------------------

    def behaviour_trust(self):

        pdr = self.df["dst_pkts"] / (self.df["src_pkts"] + 1)

        attack = self.df["label"]

        self.df["Behaviour_Trust"] = (

            0.70 * pdr +

            0.30 * (1 - attack)

        ).clip(0,1)

    # -----------------------------------
    # Resource Trust
    # -----------------------------------

    def resource_trust(self):

        load = (

            self.normalize("src_pkts")

            + self.normalize("dst_pkts")

            + self.normalize("src_bytes")

            + self.normalize("dst_bytes")

        ) / 4

        energy = 1 - load

        delay = self.normalize("duration")

        self.df["Resource_Trust"] = (

            0.60 * energy +

            0.40 * (1 - delay)

        ).clip(0,1)

    # -----------------------------------
    # Historical Trust
    # -----------------------------------

    def historical_trust(self):

        history = (

            self.normalize("src_pkts")

            + self.normalize("dst_pkts")

        ) / 2

        self.df["Historical_Trust"] = (

            1 - history

        ).clip(0,1)

    def compute(self):

        self.behaviour_trust()

        self.resource_trust()

        self.historical_trust()

        return self.df