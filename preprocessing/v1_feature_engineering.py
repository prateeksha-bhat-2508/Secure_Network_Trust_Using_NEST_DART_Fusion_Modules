import numpy as np
import pandas as pd

from utils.logger import logger


class FeatureEngineer:

    def __init__(self, df: pd.DataFrame):

        self.df = df.copy()

    def create_trust_features(self):

        np.random.seed(42)

        n = len(self.df)

        # ----------------------------
        # Residual Energy
        # ----------------------------

        self.df["Residual_Energy"] = np.random.uniform(
            0.55,
            1.0,
            n
        )

        # ----------------------------
        # Packet Delivery Ratio
        # ----------------------------

        self.df["Packet_Delivery_Ratio"] = np.random.uniform(
            0.80,
            1.0,
            n
        )

        # ----------------------------
        # Communication Reliability
        # ----------------------------

        self.df["Communication_Reliability"] = np.random.uniform(
            0.70,
            1.0,
            n
        )

        # ----------------------------
        # Delay Score
        # ----------------------------

        self.df["Delay_Score"] = np.random.uniform(
            0,
            0.30,
            n
        )

        # ----------------------------
        # Historical Trust
        # ----------------------------

        self.df["Historical_Trust"] = np.random.uniform(
            0.60,
            1.0,
            n
        )

        # ----------------------------
        # Behaviour Consistency
        # ----------------------------

        self.df["Behaviour_Consistency"] = np.random.uniform(
            0.65,
            1.0,
            n
        )

        # ----------------------------
        # Link Stability
        # ----------------------------

        self.df["Link_Stability"] = np.random.uniform(
            0.70,
            1.0,
            n
        )

        logger.info("Trust features created.")

        return self

    def create_attack_probability(self):

        if "label" in self.df.columns:

            self.df["Attack_Probability"] = self.df["label"]

        else:

            self.df["Attack_Probability"] = np.random.uniform(
                0,
                1,
                len(self.df)
            )

        logger.info("Attack probability generated.")

        return self

    def create_unified_trust_vector(self):

        self.df["Unified_Trust_Vector"] = (

            0.18 * self.df["Residual_Energy"]

            + 0.17 * self.df["Packet_Delivery_Ratio"]

            + 0.17 * self.df["Communication_Reliability"]

            + 0.14 * self.df["Historical_Trust"]

            + 0.14 * self.df["Behaviour_Consistency"]

            + 0.10 * self.df["Link_Stability"]

            - 0.10 * self.df["Delay_Score"]

        )

        logger.info("Unified Trust Vector generated.")

        return self

    def transform(self):

        return (

            self.create_trust_features()

                .create_attack_probability()

                .create_unified_trust_vector()

                .df

        )