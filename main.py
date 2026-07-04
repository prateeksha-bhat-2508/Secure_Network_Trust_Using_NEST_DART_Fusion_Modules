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
from preprocessing.trust_fusion import TrustFusion
from evaluation.metrics import Evaluation

from barm.ug import UG
from barm.ra import RA
from barm.reputation import Reputation
from barm.trust_update import TrustUpdate

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

import os
import json
import pandas as pd


def main():

    # ============================================
    # 1. LOAD DATASET
    # ============================================

    loader = DatasetLoader()
    raw_df = loader.load_dataset("Network")
    raw_df = DataCleaner(raw_df).clean()
    DataProfiler(raw_df).profile()

    # ============================================
    # 2. PREPROCESSING (per‑flow)
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
    # 3. NODE AGGREGATION
    # ============================================

    aggregator = NodeAggregator(df, raw_df)
    node_df = aggregator.aggregate()
    print("\nAggregated Nodes")
    print(node_df.head())

    # ============================================
    # 4. NETWORK GRAPH & CENTRALITY
    # ============================================

    graph_builder = NetworkGraph(raw_df, node_df)
    graph_builder.flow_df = raw_df
    graph = graph_builder.build_graph()
    node_df = graph_builder.add_centrality()          # adds Centrality_Trust

    # ============================================
    # 5. HYBRID TRUST (depends on graph & centrality)
    # ============================================

    hybrid = HybridTrust(node_df, graph)
    node_df = hybrid.compute()                       # creates Hybrid_Trust

    print("\nHybrid Trust")
    print(node_df[["Node_ID", "Hybrid_Trust"]].head())

    # ============================================
    # 6. TRUST EVIDENCE FUSION (creates Unified_Trust_Evidence)
    # ============================================

    node_df = TrustFusion(node_df).compute()

    print("\nColumns after Trust Fusion:")
    print(node_df.columns.tolist())
    print("\nTrust Fusion Output:")
    print(node_df.head())

    # ============================================
    # 7. COMPUTE NEIGHBOR_TRUST (needs graph + Hybrid_Trust)
    # ============================================

    node_ids = set(node_df["Node_ID"].astype(str))
    neighbor_trust = []

    for node in node_df["Node_ID"]:
        node_str = str(node)
        neighbors = list(graph.neighbors(node_str))
        # Keep only neighbors that are also in node_df
        present_neighbors = [n for n in neighbors if n in node_ids]
        if present_neighbors:
            avg = node_df[node_df["Node_ID"].isin(present_neighbors)]["Hybrid_Trust"].mean()
        else:
            avg = 0.0
        neighbor_trust.append(avg)

    node_df["Neighbor_Trust"] = neighbor_trust

    # ============================================
    # 8. BARM (uses Unified_Trust_Evidence & Neighbor_Trust)
    # ============================================

    node_df = UG(node_df).compute()          # creates UG
    node_df = RA(node_df).compute()          # creates RA
    node_df = Reputation(node_df).compute()  # creates Reputation
    node_df = TrustUpdate(node_df).compute() # creates BARM_Score

    print("\nBARM")
    print(
        node_df[
            [
                "Node_ID",
                "UG",
                "RA",
                "Reputation",
                "BARM_Score"
            ]
        ].head()
    )

    # ============================================
    # 9. ADRS‑MPIQ
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
    # 10. PROOF OF TRUST
    # ============================================

    node_df = TrustManager(node_df).compute()   # creates Trust_Value
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
    # 11. EVALUATION
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
    # 12. FINAL INFO & SAVE
    # ============================================

    print("\nBlockchain Valid :", valid)
    print("Consensus :", round(consensus, 4))
    print("\nFinal Shape :", node_df.shape)

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

    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score
    import nympy as np
    # Split into train (70%) and test (30%) – you have only 51 nodes, so adjust as needed
    X = node_df[["BARM_Score", "ADRS_MPIQ_Score", "Trust_Value"]]
    y = (node_df["Attack_Probability"] >= 0.5).astype(int)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=42, stratify=y
    )
    
    def find_best_threshold(y_true, y_score):
        thresholds = np.linspace(0.01, 0.99, 99)
        best_t = 0.5
        best_acc = 0
        for t in thresholds:
            pred = (y_score >= t).astype(int)
            acc = accuracy_score(y_true, pred)
            if acc > best_acc:
                best_acc = acc
                best_t = t
        return best_t

    barm_t = find_best_threshold(y_train, X_train["BARM_Score"])
    adrs_t = find_best_threshold(y_train, X_train["ADRS_MPIQ_Score"])
    prop_t = find_best_threshold(y_train, X_train["Trust_Value"])

    # Evaluate on test set
    barm_pred = (X_test["BARM_Score"] >= barm_t).astype(int)
    adrs_pred = (X_test["ADRS_MPIQ_Score"] >= adrs_t).astype(int)
    prop_pred = (X_test["Trust_Value"] >= prop_t).astype(int)

    print("BARM Test Accuracy:", accuracy_score(y_test, barm_pred))
    print("ADRS Test Accuracy:", accuracy_score(y_test, adrs_pred))
    print("Proposed Test Accuracy:", accuracy_score(y_test, prop_pred))
if __name__ == "__main__":
    main()
