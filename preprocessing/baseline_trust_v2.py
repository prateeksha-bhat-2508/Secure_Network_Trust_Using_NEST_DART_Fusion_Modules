import numpy as np
import pandas as pd


class BaselineTrust:

    def __init__(self, df):

        self.df = df.copy()

    def normalize(self, col):

        x = self.df[col].astype(float)

        if x.max() == x.min():
            return pd.Series(np.ones(len(x)), index=self.df.index)

        return (x - x.min()) / (x.max() - x.min())

    def compute(self):

        # -------------------------
        # Behaviour Trust
        # -------------------------

        state_score = self.normalize("conn_state")

        duration_score = 1 - self.normalize("duration")

        self.df["Behaviour_Trust"] = (

            0.45 * (1 - self.df["label"])

            + 0.35 * state_score

            + 0.20 * duration_score

        ).clip(0, 1)

        # -------------------------
        # Resource Trust
        # -------------------------

        byte_score = self.normalize("src_bytes") + self.normalize("dst_bytes")

        pkt_score = self.normalize("src_pkts") + self.normalize("dst_pkts")

        missed = 1 - self.normalize("missed_bytes")

        self.df["Resource_Trust"] = (

            0.40 * (byte_score / 2)

            + 0.35 * (pkt_score / 2)

            + 0.25 * missed

        ).clip(0, 1)

        # -------------------------
        # Reliability Trust
        # -------------------------

        proto = self.normalize("proto")

        service = self.normalize("service")

        self.df["Reliability_Trust"] = (

            0.40 * state_score

            + 0.30 * proto

            + 0.30 * service

        ).clip(0, 1)

        # -------------------------
        # Historical Trust
        # -------------------------

        self.df["Historical_Trust"] = (

            self.df.groupby("src_ip")["Behaviour_Trust"]

            .transform("mean")

        )

        return self.df