import numpy as np
import pandas as pd

from utils.logger import logger


class FeatureEngineer:

    def __init__(self, df):

        self.df = df.copy()

    # ----------------------------------------------------
    # Normalize helper
    # ----------------------------------------------------

    def normalize(self, column):

        col = self.df[column].astype(float)

        minimum = col.min()
        maximum = col.max()

        if maximum == minimum:
            return pd.Series(np.ones(len(col)))

        return (col - minimum) / (maximum - minimum)

    # ----------------------------------------------------
    # Residual Energy
    # ----------------------------------------------------

    def residual_energy(self):

        required = {"src_pkts", "dst_pkts", "src_bytes", "dst_bytes"}

        if required.issubset(self.df.columns):

            load = (

                self.normalize("src_pkts") +
                self.normalize("dst_pkts") +
                self.normalize("src_bytes") +
                self.normalize("dst_bytes")

            ) / 4

            self.df["Residual_Energy"] = 1 - load

        else:

            self.df["Residual_Energy"] = 0.5

        logger.info("Residual Energy calculated.")
    # ----------------------------------------------------
    # Packet Delivery Ratio
    # ----------------------------------------------------

    def packet_delivery_ratio(self):

        if {"src_pkts", "dst_pkts"}.issubset(self.df.columns):

            self.df["Packet_Delivery_Ratio"] = (

                self.df["dst_pkts"] /

                (self.df["src_pkts"] + 1)

            )

            self.df["Packet_Delivery_Ratio"] = self.df[
                "Packet_Delivery_Ratio"
            ].clip(0,1)

        else:

            self.df["Packet_Delivery_Ratio"] = 0.5

        logger.info("Packet Delivery Ratio calculated.")

    # ----------------------------------------------------
    # Delay Score
    # ----------------------------------------------------

    def delay_score(self):

        if "duration" in self.df.columns:

            self.df["Delay_Score"] = self.normalize("duration")
        else:

            self.df["Delay_Score"] = 0.5
        logger.info("Delay Score calculated.")

    # ----------------------------------------------------
    # Communication Reliability
    # ----------------------------------------------------

    def communication_reliability(self):

        score = np.zeros(len(self.df))

        if "conn_state" in self.df.columns:

            state = self.df["conn_state"]

            score += (

                state /

                state.max()

            )

        if "service" in self.df.columns:

            service = self.df["service"]

            score += (

                service /

                service.max()

            )

        if "proto" in self.df.columns:

            proto = self.df["proto"]

            score += (

                proto /

                proto.max()

            )

        self.df["Communication_Reliability"] = score / 3

        logger.info("Communication Reliability calculated.")

    # ----------------------------------------------------
    # Historical Trust
    # ----------------------------------------------------

    def historical_trust(self):

        if "ct_srv_src" in self.df.columns:

            self.df["Historical_Trust"] = 1 - self.normalize("ct_srv_src")

        elif "ct_dst_src_ltm" in self.df.columns:

            self.df["Historical_Trust"] = 1 - self.normalize("ct_dst_src_ltm")

        else:

            self.df["Historical_Trust"] = 0.5

        logger.info("Historical Trust calculated.")

    # ----------------------------------------------------
    # Behaviour Consistency
    # ----------------------------------------------------

    def behaviour_consistency(self):

        if "label" in self.df.columns:

            self.df["Behaviour_Consistency"] = 1 - self.df["label"]

        else:

            self.df["Behaviour_Consistency"] = 0.5

        logger.info("Behaviour Consistency calculated.")

    # ----------------------------------------------------
    # Link Stability
    # ----------------------------------------------------

    def link_stability(self):

        if "ct_state_ttl" in self.df.columns:

            self.df["Link_Stability"] = self.normalize("ct_state_ttl")

        elif "sttl" in self.df.columns:

            self.df["Link_Stability"] = self.normalize("sttl")

        else:

            self.df["Link_Stability"] = 0.5

        logger.info("Link Stability calculated.")

    # ----------------------------------------------------
    # Attack Probability
    # ----------------------------------------------------

    def attack_probability(self):

        if "Predicted_Attack_Probability" in self.df.columns:

            self.df["Attack_Probability"] = self.df["Predicted_Attack_Probability"]

        else:

            self.df["Attack_Probability"] = self.df["label"]

        logger.info("Attack Probability calculated.")

    # ----------------------------------------------------
    # Unified Trust Vector
    # ----------------------------------------------------

    def unified_trust_vector(self):

        self.df["Unified_Trust_Vector"] = (

            0.18 * self.df["Residual_Energy"]

            + 0.18 * self.df["Packet_Delivery_Ratio"]

            + 0.16 * self.df["Communication_Reliability"]

            + 0.14 * self.df["Historical_Trust"]

            + 0.14 * self.df["Behaviour_Consistency"]

            + 0.10 * self.df["Link_Stability"]

            - 0.10 * self.df["Delay_Score"]

        )

        self.df["Unified_Trust_Vector"] = np.clip(

            self.df["Unified_Trust_Vector"],

            0,

            1

        )

        logger.info("Unified Trust Vector created.")

    # ----------------------------------------------------
    # Main
    # ----------------------------------------------------
   
    def transform(self):

        self.residual_energy()

        self.packet_delivery_ratio()

        self.delay_score()

        self.communication_reliability()

        self.historical_trust()

        self.behaviour_consistency()

        self.link_stability()

        self.attack_probability()

        self.behaviour_trust()

        self.resource_trust()

        self.historical_trust_layer()

        self.unified_trust_vector()

        self.generate_trust_evidence_vector()

        self.compute_trust_score()

        return self.df
        
    def behaviour_trust(self):

        self.df["Behaviour_Trust"] = (

            0.40 * self.df["Behaviour_Consistency"]

            + 0.35 * self.df["Packet_Delivery_Ratio"]

            + 0.25 * (1 - self.df["Attack_Probability"])

        )

        self.df["Behaviour_Trust"] = self.df["Behaviour_Trust"].clip(0,1)

        logger.info("Behaviour Trust calculated.")

    def resource_trust(self):

        self.df["Resource_Trust"] = (

            0.45 * self.df["Residual_Energy"]

            + 0.30 * self.df["Communication_Reliability"]

            + 0.25 * (1 - self.df["Delay_Score"])

        )

        self.df["Resource_Trust"] = self.df["Resource_Trust"].clip(0,1)

        logger.info("Resource Trust calculated.")


    def historical_trust_layer(self):

        self.df["Historical_Trust_Layer"] = (

            0.60 * self.df["Historical_Trust"]

            + 0.40 * self.df["Link_Stability"]

        )

        self.df["Historical_Trust_Layer"] = self.df["Historical_Trust_Layer"].clip(0,1)

        logger.info("Historical Trust Layer calculated.")


    def unified_trust_vector(self):

        self.df["Unified_Trust_Vector"] = (

            0.40 * self.df["Behaviour_Trust"]

            + 0.35 * self.df["Resource_Trust"]

            + 0.25 * self.df["Historical_Trust_Layer"]

        )

        self.df["Unified_Trust_Vector"] = self.df["Unified_Trust_Vector"].clip(0,1)

        logger.info("Unified Trust Vector generated.")

    def generate_trust_evidence_vector(self):

        self.df["TEV_Behaviour"] = self.df["Behaviour_Trust"]

        self.df["TEV_Resource"] = self.df["Resource_Trust"]

        self.df["TEV_Historical"] = self.df["Historical_Trust_Layer"]

        self.df["TEV_Attack"] = 1 - self.df["Attack_Probability"]

        self.df["TEV_Communication"] = self.df["Communication_Reliability"]

        self.df["TEV_PDR"] = self.df["Packet_Delivery_Ratio"]

        logger.info("Trust Evidence Vector generated.")

        return self

    def compute_trust_score(self):

        evidence = [

            "TEV_Behaviour",

            "TEV_Resource",

            "TEV_Historical",

            "TEV_Attack",

            "TEV_Communication",

            "TEV_PDR"

        ]

        self.df["Trust_Score"] = self.df[evidence].mean(axis=1)

        logger.info("Trust Score calculated from Trust Evidence.")

        return self