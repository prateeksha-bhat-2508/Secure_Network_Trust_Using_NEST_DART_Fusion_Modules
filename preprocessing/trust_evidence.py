from preprocessing.trust_evidence import TrustEvidence


class TrustEvidenceBuilder:

    def __init__(self, df):

        self.df = df

    def build(self):

        evidence = []

        for idx, row in self.df.iterrows():

            evidence.append(

                TrustEvidence(

                    node_id=idx,

                    behaviour_trust=row["Behaviour_Trust"],

                    resource_trust=row["Resource_Trust"],

                    historical_trust=row["Historical_Trust_Layer"],

                    communication_reliability=row["Communication_Reliability"],

                    packet_delivery_ratio=row["Packet_Delivery_Ratio"],

                    attack_probability=row["Attack_Probability"],

                    trust_score=row["Trust_Score"]

                )

            )

        return evidence