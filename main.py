from preprocessing.loader import DatasetLoader
from preprocessing.cleaner import DataCleaner
from preprocessing.encoder import DataEncoder
from preprocessing.scaler import DataScaler
from preprocessing.feature_engineering import FeatureEngineer
from preprocessing.baseline_trust_v2 import BaselineTrust
from preprocessing.node_aggregation import NodeAggregator
from preprocessing.network_graph import NetworkGraph
from preprocessing.hybrid_trust_v2 import HybridTrust
from preprocessing.data_profiler import DataProfiler
from evaluation.metrics import Evaluation

from preprocessing.trust_fusion import TrustFusion

from barm.ug import UG
from barm.ra import RA
from barm.reputation import Reputation
from barm.trust_update import TrustUpdate
from barm.tps import TPS


from adrs_mpiq.routing import Routing
from adrs_mpiq.queue_manager import QueueManager
from adrs_mpiq.fitness import Fitness
from adrs_mpiq.clustering import Clustering
from adrs_mpiq.encryption import Encryption
from adrs_mpiq.mpiq import MPIQ

from proof_of_trust.trust_manager import TrustManager
from proof_of_trust.ledger import Ledger
from proof_of_trust.verification import Verification
from proof_of_trust.consensus import Consensus
def main():

    # ============================================
    # Load Dataset
    # ============================================

    loader = DatasetLoader()

    raw_df = loader.load_dataset("Network")

    raw_df = DataCleaner(raw_df).clean()

    DataProfiler(raw_df).profile()

    # ============================================
    # Preprocessing
    # ============================================

    df = raw_df.copy()

    df = DataEncoder(df).encode()

    df = DataScaler(df).scale()

    from ml.predict_attack import predict_attack_probability

    df["Predicted_Attack_Probability"] = predict_attack_probability(df)

    print("\nPredicted Attack Probability")
    print(df["Predicted_Attack_Probability"].head())

    df = FeatureEngineer(df).transform()

    df = BaselineTrust(df).compute()

    print("\nBaseline Trust")
    print(
        df[
            [
                "Behaviour_Trust",
                "Resource_Trust",
                "Reliability_Trust",
                "Historical_Trust",
            ]
        ].head()
    )

    # ============================================
    # Node Aggregation
    # ============================================

    aggregator = NodeAggregator(df, raw_df)

    node_df = aggregator.aggregate()

    print("\nAggregated Nodes")
    print(node_df.head())

    # ============================================
    # Network Graph
    # ============================================

    graph_builder = NetworkGraph(raw_df, node_df)

    graph_builder.flow_df = raw_df

    graph = graph_builder.build_graph()

    node_df = graph_builder.add_centrality()

    print("\nCentrality")
    print(
        node_df[
            [
                "Node_ID",
                "Centrality_Trust"
            ]
        ].head()
    )

    # ============================================
    # Hybrid Trust
    # ============================================

    hybrid = HybridTrust(node_df, graph)

    node_df = hybrid.compute()

    print("\nHybrid Trust")
    print(
        node_df[
            [
                "Node_ID",
                "Hybrid_Trust"
            ]
        ].head()
    )

    # ============================================
    # Trust Evidence Fusion (TEFL)
    # ============================================

   

    node_df = TrustFusion(node_df).compute()

    print("\nColumns after Trust Fusion:")
    print(node_df.columns.tolist())

    print("\nTrust Fusion Output:")
    print(node_df.head())

    # ============================================
    # BARM
    # ============================================

    node_df = UG(node_df).compute()

    node_df = RA(node_df).compute()

    node_df = Reputation(node_df).compute()

    node_df = TrustUpdate(node_df).compute()

    node_df = TPS(node_df).compute()

    print("\nBARM")
    print(
        node_df[
            [
                "Node_ID",
                "UG",
                "RA",
                "Reputation",
                "Updated_Trust",
                "BARM_Score"
            ]
        ].head()
    )

    # ============================================
    # ADRS-MPIQ
    # ============================================

    node_df = Routing(node_df).compute()

    node_df = QueueManager(node_df).compute()

    node_df = Fitness(node_df).compute()

    node_df = Clustering(node_df).compute()

    node_df = Encryption(node_df).compute()

    node_df = MPIQ(node_df).compute()

    print("\nADRS-MPIQ")
    print(
        node_df[
            [
                "Node_ID",
                "Routing_Score",
                "Fitness",
                "ADRS_MPIQ_Score"
            ]
        ].head()
    )

        # ============================================
    # Proof of Trust
    # ============================================

    node_df = TrustManager(node_df).compute()

    blockchain = Ledger(node_df).generate()

    valid = Verification(blockchain).verify()

    consensus = Consensus(blockchain).compute()

    print(
    node_df[
        [
            "BARM_Score",
            "ADRS_MPIQ_Score",
            "Trust_Value"
        ]
    ].head(20)
)
    # ============================================
    # Evaluation
    # ============================================

    node_df["Consensus"] = consensus

    evaluation = Evaluation(node_df)

    barm_metrics = evaluation.compute("BARM_Score")

    adrs_metrics = evaluation.compute("ADRS_MPIQ_Score")

    proposed_metrics = evaluation.compute("Trust_Value")

    print("\n")
    print("=" * 95)
    print("FINAL COMPARISON")
    print("=" * 95)

    header = f"{'Metric':30}{'BARM':>15}{'AdRS-MPIQ':>18}{'Proposed':>18}"
    print(header)
    print("-" * 95)

    for metric in barm_metrics.keys():

        print(
            f"{metric:30}"
            f"{barm_metrics[metric]:>15.4f}"
            f"{adrs_metrics[metric]:>18.4f}"
            f"{proposed_metrics[metric]:>18.4f}"
        )

    # ============================================
    # Final Information
    # ============================================

    print("\nBlockchain Valid :", valid)

    print("Consensus :", round(consensus, 4))

    print("\nFinal Shape :", node_df.shape)


    import os
    import json
    import pandas as pd

    os.makedirs("results", exist_ok=True)

    node_df.to_csv("results/final_results.csv", index=False)

    metrics_df = pd.DataFrame({
        "Metric": list(barm_metrics.keys()),
        "BARM": list(barm_metrics.values()),
        "AdRS-MPIQ": list(adrs_metrics.values()),
        "Proposed": list(proposed_metrics.values())
    })

    metrics_df.to_csv("results/metrics.csv", index=False)

    with open("results/blockchain.json", "w") as f:
        json.dump(blockchain, f, indent=4)

if __name__ == "__main__":
    main()