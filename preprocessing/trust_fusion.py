import numpy as np


import numpy as np

class TrustFusion:

    def __init__(self, node_df):
        self.df = node_df.copy()

    def compute(self):

        # -------------------------------
        # Trust Evidence Vector
        # -------------------------------

        self.df["Evidence_Vector"] = (

            0.35*self.df["Hybrid_Trust"]

            +0.25*self.df["Behaviour_Trust"]

            +0.15*self.df["Resource_Trust"]

            +0.15*self.df["Reliability_Trust"]

            +0.10*self.df["Centrality_Trust"]

        ).clip(0,1)

        # -------------------------------
        # Evidence Confidence
        # -------------------------------

        self.df["Evidence_Confidence"] = (

            0.60*self.df["Historical_Trust"]

            +0.40*self.df["Neighbor_Trust"]

        ).clip(0,1)

        # -------------------------------
        # Unified Trust Evidence
        # -------------------------------

        self.df["Unified_Trust_Evidence"] = (

            0.70*self.df["Evidence_Vector"]

            +0.30*self.df["Evidence_Confidence"]

        ).clip(0,1)

        return self.df