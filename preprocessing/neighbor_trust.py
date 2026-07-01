import numpy as np


class NeighborTrust:

    def __init__(self, graph, node_df):

        self.graph = graph
        self.node_df = node_df.copy()

    def compute(self):

        trust_lookup = dict(
            zip(
                self.node_df["Node_ID"],
                self.node_df["Direct_Trust"]
            )
        )

        neighbor_scores = []

        for node in self.node_df["Node_ID"]:

            if node not in self.graph:

                neighbor_scores.append(
                    trust_lookup[node]
                )

                continue

            neighbors = list(
                self.graph.neighbors(node)
            )

            if len(neighbors) == 0:

                neighbor_scores.append(
                    trust_lookup[node]
                )

                continue

            values = []

            for n in neighbors:

                if n in trust_lookup:

                    values.append(
                        trust_lookup[n]
                    )

            if len(values) == 0:

                avg = trust_lookup[node]

            else:

                avg = np.mean(values)

            final = (

                0.6 * trust_lookup[node]

                + 0.4 * avg

            )

            neighbor_scores.append(final)

        self.node_df["Neighbor_Trust"] = neighbor_scores

        return self.node_df