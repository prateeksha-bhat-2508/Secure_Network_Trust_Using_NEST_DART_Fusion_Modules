import numpy as np
import pandas as pd


class HybridTrust:

    def __init__(self, node_df, graph):

        self.df = node_df.copy()
        self.graph = graph

    def compute(self):

        # =====================================
        # Direct Trust
        # =====================================

        self.df["Direct_Trust"] = (

            0.45 * self.df["Behaviour_Trust"]

            + 0.30 * self.df["Reliability_Trust"]

            + 0.15 * self.df["Resource_Trust"]

            + 0.10 * self.df["Historical_Trust"]

        ).clip(0, 1)

        # =====================================
        # Neighbor Trust
        # =====================================

        lookup = dict(
            zip(
                self.df["Node_ID"],
                self.df["Direct_Trust"]
            )
        )

        neighbor_scores = []

        for node in self.df["Node_ID"]:

            if node not in self.graph:

                neighbor_scores.append(
                    lookup[node]
                )

                continue

            neighbors = list(self.graph.neighbors(node))

            if len(neighbors) == 0:

                neighbor_scores.append(
                    lookup[node]
                )

                continue

            values = []

            for n in neighbors:

                if n in lookup:

                    values.append(lookup[n])

            if len(values) == 0:

                avg = lookup[node]

            else:

                avg = np.mean(values)

            score = (

                0.60 * lookup[node]

                + 0.40 * avg

            )

            neighbor_scores.append(score)

        self.df["Neighbor_Trust"] = neighbor_scores

        # =====================================
        # Hybrid Trust
        # =====================================

        if "Centrality_Trust" not in self.df.columns:

            self.df["Centrality_Trust"] = 0.5

        self.df["Hybrid_Trust"] = (

            0.40 * self.df["Neighbor_Trust"]

            + 0.25 * self.df["Direct_Trust"]

            + 0.20 * self.df["Resource_Trust"]

            + 0.15 * self.df["Centrality_Trust"]

        ).clip(0, 1)

        return self.df