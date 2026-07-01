import pandas as pd


class HybridTrustAggregation:

    def __init__(self, node_df: pd.DataFrame):

        self.node_df = node_df.copy()

    def aggregate(self):

        # ------------------------------------------
        # Hybrid Trust Equation
        # ------------------------------------------
        #
        # T_hybrid =
        # 0.40 * Neighbor Trust
        # +0.25 * Direct Trust
        # +0.20 * Reliability Trust
        # +0.15 * Centrality Trust
        #
        # ------------------------------------------

        self.node_df["Hybrid_Trust"] = (

            0.40 * self.node_df["Neighbor_Trust"]

            + 0.25 * self.node_df["Direct_Trust"]

            + 0.20 * self.node_df["Reliability_Trust"]

            + 0.15 * self.node_df["Centrality_Trust"]

        ).clip(0, 1)

        return self.node_df