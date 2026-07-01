class NodeAggregator:

    def __init__(self, trust_df, raw_df):

        self.trust_df = trust_df.copy()

        self.raw_df = raw_df.copy()

    def aggregate(self):

        self.trust_df["Node_ID"] = self.raw_df["src_ip"].values

        grouped = self.trust_df.groupby("Node_ID").agg({

            "Behaviour_Trust": "mean",

            "Resource_Trust": "mean",

            "Reliability_Trust": "mean",

            "Historical_Trust": "mean",

            "label": "mean"

        }).reset_index()

        grouped.rename(
            columns={
                "label": "Attack_Probability"
            },
            inplace=True
        )

        return grouped