<div align="center">

# 🔐 BARM_vs_AdRS-MPIQ
### A Machine Learning Assisted Hybrid Trust Evaluation Framework for Secure IoT Networks using Trust Evidence Fusion, BARM, AdRS-MPIQ and Blockchain-based Proof of Trust

<img src="https://img.shields.io/badge/Python-3.11+-blue?logo=python">
<img src="https://img.shields.io/badge/Streamlit-Dashboard-red?logo=streamlit">
<img src="https://img.shields.io/badge/XGBoost-Intrusion%20Detection-success">
<img src="https://img.shields.io/badge/Blockchain-Proof%20of%20Trust-yellow">
<img src="https://img.shields.io/badge/Network-IoT-orange">
<img src="https://img.shields.io/badge/License-MIT-green">

---

**A Next-Generation Trust Evaluation Framework integrating Machine Learning, Trust Evidence Fusion, Hybrid Trust Computation, BARM, AdRS-MPIQ Routing Optimization and Blockchain-based Trust Validation for Secure IoT Networks.**

</div>

---

# 📖 Abstract

Internet of Things (IoT) environments are increasingly deployed in smart homes, healthcare, industrial automation, transportation, and critical infrastructure. While these interconnected devices enable intelligent automation and real-time communication, they also introduce significant security challenges due to their heterogeneous nature, limited computational resources, and vulnerability to sophisticated cyber attacks.

Traditional trust evaluation techniques primarily rely on static trust metrics or historical interactions, making them less effective against dynamic adversarial behaviors and evolving attack patterns. Existing approaches such as BARM, AdRS-MPIQ, and Proof of Trust each address specific aspects of trust management; however, none of them provide a unified framework capable of integrating trust evidence, routing intelligence, blockchain validation, and machine learning-based attack prediction.

This project proposes a **Machine Learning Assisted Hybrid Trust Evaluation Framework** that combines multiple trust evaluation methodologies into a single architecture. The proposed framework introduces a **Trust Evidence Fusion Layer (TEFL)** that aggregates behavioral, resource, communication, historical, and attack-related evidence to generate a comprehensive trust representation for every IoT node.

Unlike conventional systems, the proposed framework integrates an **XGBoost-based Intrusion Detection Module** trained on more than **2.8 million network flows from the CIC-IDS2017 benchmark dataset**. Instead of relying solely on static attack labels, the trained model predicts attack probabilities for incoming network traffic, which are then incorporated as an additional trust evidence source inside the TEFL layer.

The generated trust values are subsequently refined using **Hybrid Trust Computation**, evaluated through the **BARM trust management framework**, optimized using **AdRS-MPIQ routing mechanisms**, and finally secured through a **Blockchain-based Proof of Trust** architecture. An interactive Streamlit dashboard provides comprehensive visualization of trust analytics, blockchain validation, routing performance, network topology, and machine learning metrics.

The proposed architecture demonstrates how machine learning and trust computation can be seamlessly integrated to provide a scalable, adaptive, and secure trust management framework for modern IoT environments.

---

# 🎯 Problem Statement

Traditional IoT trust management mechanisms suffer from several limitations:

- Static trust computation without adaptive learning.
- Dependence on manually defined trust metrics.
- Lack of attack prediction capabilities.
- Poor integration between routing and trust evaluation.
- Absence of blockchain-based trust validation.
- Limited explainability of trust decisions.
- Inability to effectively handle large-scale dynamic IoT environments.

These limitations motivate the development of a unified framework capable of integrating machine learning, trust evidence fusion, blockchain validation, and intelligent routing into a single trust evaluation architecture.

---

# 💡 Proposed Solution

The proposed framework introduces a **multi-layer trust evaluation architecture** that combines:

- Hybrid Trust Computation
- Trust Evidence Fusion Layer (TEFL)
- Blockchain-based Anti-aggregation Reputation Management (BARM)
- AdRSE = Adaptive Rivest Shamir Advanced Encryption Standard (the hybrid encryption algorithm)
- MPIQ = Multi-Parameter Ideative Queuing algorithm (used for cluster-head selection and optimal routing)
- Blockchain-based Proof of Trust
- Machine Learning Assisted Intrusion Detection using XGBoost

The framework computes trust values by simultaneously considering:

- Behavioral Trust
- Resource Trust
- Historical Trust
- Communication Reliability
- Network Centrality
- Routing Efficiency
- Machine Learning Predicted Attack Probability
- Blockchain Consensus

The final trust score represents a comprehensive measure of node reliability, making the framework suitable for secure routing, node authentication, and malicious node detection in IoT networks.

---

# ⭐ Novel Contributions

Unlike the original research papers, this implementation introduces several significant improvements:

## ✅ Trust Evidence Fusion Layer (TEFL)

A novel trust evidence fusion mechanism is proposed to combine multiple heterogeneous trust metrics into a unified trust representation.

The TEFL layer aggregates:

- Behavioral Trust
- Resource Trust
- Historical Trust
- Communication Reliability
- Packet Delivery Ratio
- Link Stability
- Machine Learning Attack Probability

into a single **Unified Trust Evidence Score**.

---

## ✅ Machine Learning Assisted Trust Evaluation

Instead of assigning attack probabilities directly from dataset labels, an **XGBoost Intrusion Detection Model** is trained using the **CIC-IDS2017 benchmark dataset (2.8+ Million network flows)**.

The trained model predicts the probability that each incoming network flow is malicious.

These predicted probabilities are injected into the Trust Evidence Fusion Layer, enabling trust computation to adapt according to machine learning predictions rather than static labels.

---

## ✅ Hybrid Trust Computation

The framework introduces a hybrid trust computation strategy by combining:

- Direct Trust
- Neighbor Trust
- Network Centrality
- Historical Trust

to produce a robust trust estimation for every IoT node.

This significantly improves resilience against isolated malicious behaviors and network topology changes.

---

## ✅ Integrated BARM Framework

The classical Blockchain-based Attack Reputation Model is enhanced by incorporating:

- Unified Trust Evidence
- Hybrid Trust
- Reputation Average
- Trust Propagation
- Updated Trust Scores

to improve attack resilience and trust estimation accuracy.

---

## ✅ Enhanced AdRS-MPIQ Routing

The routing framework integrates:

- Queue Management
- Intelligent Fitness Evaluation
- Secure Routing Scores
- Adaptive Clustering
- Encryption-aware Communication

to improve routing reliability while minimizing communication overhead.

---

## ✅ Blockchain-based Proof of Trust

Every finalized trust score is permanently validated using a lightweight blockchain implementation.

Each blockchain block stores:

- Node Identifier
- Trust Value
- Hash
- Previous Hash
- Timestamp

A Merkle Tree is generated to verify data integrity, while consensus algorithms ensure trustworthy validation across the network.

---

## ✅ Interactive Analytics Dashboard

A complete Streamlit-based visualization dashboard has been developed featuring:

- Network Overview
- Trust Analytics
- TEFL Visualization
- Hybrid Trust Analysis
- BARM Performance
- AdRS-MPIQ Analysis
- Blockchain Explorer
- Merkle Tree Visualization
- Network Graph
- XGBoost Intrusion Detection Metrics
- Comparative Framework Evaluation

making the proposed framework suitable for both research and practical demonstrations.

---

# 🚀 Key Features

- Hybrid Trust Evaluation
- Trust Evidence Fusion Layer
- BARM Trust Management
- AdRS-MPIQ Secure Routing
- Blockchain-based Proof of Trust
- XGBoost Intrusion Detection
- Machine Learning Assisted Trust Prediction
- Network Centrality Analysis
- Interactive Streamlit Dashboard
- Blockchain Explorer
- Merkle Tree Visualization
- Comparative Framework Analysis
- Automated Evaluation Metrics
- Real-time Trust Computation
- Modular Research Architecture

---

# 🏗️ System Architecture

The proposed framework follows a modular layered architecture where each component performs a specialized task before passing its output to the next layer.

```text
                                ┌─────────────────────────────┐
                                │     Network Dataset         │
                                │ (train_test_network.csv)    │
                                └──────────────┬──────────────┘
                                               │
                                               ▼
                                ┌─────────────────────────────┐
                                │      Data Preprocessing     │
                                │ • Cleaning                  │
                                │ • Encoding                  │
                                │ • Scaling                   │
                                └──────────────┬──────────────┘
                                               │
                                               ▼
                     ┌─────────────────────────────────────────────────┐
                     │ Machine Learning Intrusion Detection (XGBoost)   │
                     │ Trained on CIC-IDS2017 (2.8+ Million Flows)      │
                     └──────────────┬───────────────────────────────────┘
                                    │
                         Predicted Attack Probability
                                    │
                                    ▼
                      ┌────────────────────────────────┐
                      │      Feature Engineering       │
                      │ Behaviour Features             │
                      │ Resource Features              │
                      │ Historical Features            │
                      │ Communication Features         │
                      └──────────────┬─────────────────┘
                                     │
                                     ▼
                      ┌────────────────────────────────┐
                      │      Hybrid Trust Engine        │
                      └──────────────┬─────────────────┘
                                     │
                                     ▼
                 ┌───────────────────────────────────────────┐
                 │ Trust Evidence Fusion Layer (TEFL)         │
                 └──────────────┬────────────────────────────┘
                                │
                ┌───────────────┴───────────────────┐
                ▼                                   ▼
        ┌───────────────┐                 ┌────────────────┐
        │     BARM      │                 │  AdRS-MPIQ     │
        └───────┬───────┘                 └────────┬───────┘
                │                                  │
                └───────────────┬──────────────────┘
                                ▼
                ┌────────────────────────────────┐
                │ Proof of Trust Blockchain      │
                └──────────────┬─────────────────┘
                               ▼
                ┌────────────────────────────────┐
                │ Streamlit Analytics Dashboard  │
                └────────────────────────────────┘
```

---

# 🔄 Complete Workflow

The framework performs trust evaluation in multiple stages.

## Step 1 — Dataset Loading

The network traffic dataset is loaded from the preprocessing module.

The framework currently supports

- Network Dataset
- UNSW-NB15 Training Dataset
- UNSW-NB15 Testing Dataset
- Multiple IoT datasets
- CIC-IDS2017 (Machine Learning Module)

The preprocessing pipeline automatically validates dataset availability before execution.

---

## Step 2 — Data Cleaning

The cleaning module performs

- Duplicate removal
- Missing value handling
- Constant feature removal
- Data validation

This ensures that noisy network records do not influence trust computation.

---

## Step 3 — Encoding

Network traffic contains several categorical attributes such as

- Protocol
- Service
- Connection State
- DNS Information
- SSL Attributes
- HTTP Features

These categorical values are converted into numerical representations using **Label Encoding**, allowing them to be processed by machine learning algorithms and trust models.

---

## Step 4 — Feature Scaling

Different network attributes possess different numerical ranges.

For example,

- Duration
- Packet Count
- Packet Size

cannot be compared directly.

The framework therefore performs **Min-Max Normalization** using

\[
x'=\frac{x-x_{min}}{x_{max}-x_{min}}
\]

which transforms every numerical feature into the range

\[
0 \le x \le 1
\]

ensuring fair contribution during trust computation.

---

# 🤖 Machine Learning Assisted Intrusion Detection

Unlike conventional trust frameworks, the proposed architecture introduces an independent Machine Learning module.

## Training Dataset

The XGBoost classifier is trained using

**CIC-IDS2017**

containing over

- 2.8 Million Network Flows
- Multiple attack categories
- Benign traffic

The model learns complex attack patterns that cannot be captured using manually defined rules.

---

## Inference Dataset

During execution,

the trained XGBoost model predicts attack probabilities for

**train_test_network.csv**

instead of relying on dataset labels.

This enables

- adaptive trust estimation
- realistic attack prediction
- dynamic trust computation

---

## Why XGBoost?

XGBoost was selected because it provides

- Extremely high classification accuracy
- Fast inference
- Excellent handling of imbalanced datasets
- Low computational overhead
- High scalability
- Feature importance estimation

Compared to traditional classifiers, XGBoost performs exceptionally well for intrusion detection problems involving heterogeneous network traffic.

---

## XGBoost Integration

Instead of computing

```text
Attack Probability = Dataset Label
```

the proposed framework performs

```text
Network Traffic
       │
       ▼
XGBoost Prediction
       │
       ▼
Predicted Attack Probability
       │
       ▼
Feature Engineering
       │
       ▼
Trust Evidence Fusion
```

The predicted attack probability becomes an additional trust evidence source inside TEFL.

This makes the framework adaptive to previously unseen network behaviour.

---

# 🧩 Feature Engineering

The feature engineering module constructs several trust attributes required by later stages.

These include

## Behaviour Trust

Measures node behaviour consistency based on

- Packet Delivery Ratio
- Attack Probability
- Behaviour Consistency

Higher behaviour trust indicates reliable communication behaviour.

---

## Resource Trust

Represents node resource availability using

- Residual Energy
- Communication Reliability
- Delay Score

Nodes with stable resources receive higher trust.

---

## Historical Trust

Historical interactions are incorporated to prevent trust fluctuation.

Frequently reliable nodes maintain higher trust values.

---

## Link Stability

Measures communication consistency using

- TTL
- Network statistics
- Connection history

Stable communication links receive higher trust scores.

---

## Communication Reliability

Communication reliability evaluates

- Successful communication
- Routing consistency
- Service stability

Reliable communication increases overall trust.

---

# 🔀 Hybrid Trust Computation

Hybrid Trust combines multiple trust sources instead of relying on a single metric.

The framework computes

```text
Hybrid Trust

=

Behaviour Trust
+
Historical Trust
+
Centrality Trust
+
Neighbour Trust
```

Hybrid Trust significantly improves robustness against

- malicious forwarding
- temporary failures
- routing instability
- isolated attacks

---

# 🌐 Trust Evidence Fusion Layer (TEFL)

TEFL is the core contribution of this project.

Instead of evaluating trust using one metric,

TEFL fuses multiple trust evidences into a unified representation.

Input evidences include

- Behaviour Trust
- Resource Trust
- Historical Trust
- Communication Reliability
- Packet Delivery Ratio
- Link Stability
- Machine Learning Attack Probability

The output is

```text
Unified Trust Evidence
```

which becomes the primary trust representation used throughout the remaining framework.

---

# 🧮 Trust Score Computation

The final trust score is computed by combining

- Unified Trust Evidence
- Hybrid Trust
- Routing Trust
- Reputation
- Blockchain Validation

The resulting score satisfies

```text
0 ≤ Trust ≤ 1
```

where

- 1 indicates highly trusted nodes
- 0 indicates malicious nodes

The trust score continuously adapts according to current network behaviour.

---

---

# 🔄 Complete Workflow

The complete execution pipeline of the project is illustrated below.

```text
               Raw Network Dataset
        (UNSW-NB15 + CICIDS2017)
                     │
                     ▼
          Data Loading & Cleaning
                     │
                     ▼
       Encoding + Feature Engineering
                     │
                     ▼
           Feature Scaling Pipeline
                     │
                     ▼
        Hybrid Trust Computation Engine
                     │
       ┌─────────────┼─────────────┐
       ▼             ▼             ▼
    BARM         AdRS-MPIQ     Baseline Models
       │             │             │
       └─────────────┼─────────────┘
                     ▼
          Trust & Routing Decisions
                     │
                     ▼
       XGBoost Intrusion Detection
                     │
                     ▼
        Blockchain Transaction Layer
                     │
                     ▼
        Proof of Trust Verification
                     │
                     ▼
      Performance Evaluation Engine
                     │
                     ▼
        Interactive Streamlit Dashboard
```

---

# 🧠 Machine Learning Pipeline

The machine learning engine performs intelligent intrusion detection before trust-based routing.

### Step 1 — Dataset Loading

The framework loads:

- UNSW-NB15 Dataset
- CICIDS2017 Dataset

Both datasets are cleaned and transformed into a unified format.

---

### Step 2 — Data Cleaning

The preprocessing module

- removes missing values
- removes infinite values
- removes duplicates
- standardizes column names
- converts datatypes

---

### Step 3 — Encoding

Categorical values are converted into numerical form.

Examples include

- protocol
- service
- connection state
- DNS attributes
- SSL attributes
- HTTP attributes

using Label Encoding.

---

### Step 4 — Feature Scaling

Numerical features are normalized using StandardScaler.

This improves

- convergence
- model stability
- prediction consistency

---

### Step 5 — Feature Engineering

Additional network statistics are generated including

- Trust Indicators
- Hybrid Trust Score
- Traffic Statistics
- Flow Aggregations
- Packet Features

---

### Step 6 — XGBoost Prediction

The processed features are passed into the trained XGBoost classifier.

Outputs include

- Attack Probability
- Binary Attack Prediction
- Confidence Score

These predictions are then fused with the trust engine before routing decisions are made.

---

# 🛡 Hybrid Trust Management

Unlike conventional systems that rely on a single trust metric, this framework combines multiple trust evidence sources.

## Baseline Trust

Computes the initial trust value using

- historical behaviour
- communication history
- interaction success

---

## Neighbor Trust

Nodes evaluate neighbouring nodes.

Parameters include

- forwarding behaviour
- successful transmission
- packet delivery

---

## Hybrid Trust

Hybrid trust combines

- Baseline Trust
- Neighbor Trust
- Network Behaviour
- Machine Learning Prediction

into a unified trust score.

---

## Trust Fusion

Multiple trust scores are aggregated into one final trust value.

This minimizes

- false trust
- malicious recommendations
- trust fluctuation

---

# 🔐 BARM Engine

The BARM engine evaluates node reliability before routing.

Components include

## Reputation Analysis

Computes historical reputation.

## Trust Prediction Score (TPS)

Predicts future trustworthiness.

## Utility Gain (UG)

Measures communication usefulness.

## Reputation Adjustment (RA)

Penalizes malicious behaviour.

## Trust Update

Continuously updates node trust after every interaction.

---

# 🚀 AdRS-MPIQ Routing Engine

The routing engine performs intelligent secure routing.

It consists of

### Cluster Head Selection

Nodes are selected using

- Delay
- Residual Energy
- Distance
- Trust Score

---

### MPIQ Optimization

Uses Multi-Parameter Ideative Queuing optimization for

- Cluster Head Selection
- Path Selection
- Load Balancing

---

### Adaptive Encryption

Before transmission,

packets are encrypted using

AdRSE

which combines

- RSA
- AES
- Adaptive Key Generation

to provide secure communication.

---

# ⛓ Blockchain Layer

Every routing decision is recorded on a lightweight blockchain.

Each block stores

- Sender Node
- Receiver Node
- Trust Score
- Timestamp
- Hash
- Previous Hash

Benefits include

- Tamper resistance
- Immutable records
- Secure verification
- Distributed trust

---

# ✅ Proof of Trust Consensus

Instead of Proof of Work,

this framework implements

Proof of Trust.

Consensus depends on

- Node Trust
- Reputation
- Routing Behaviour
- Historical Performance

This significantly reduces

- computational overhead
- energy consumption
- verification latency

---

# 📊 Evaluation Metrics

The project evaluates multiple performance indicators.

| Category | Metrics |
|----------|----------|
| Machine Learning | Accuracy, Precision, Recall, F1 Score |
| Trust | Average Trust, Trust Distribution |
| Routing | Delay, Packet Delivery Ratio, Throughput |
| Security | Attack Detection Rate, Malicious Nodes |
| Blockchain | Block Generation, Verification |
| Network | Energy Consumption, Lifetime |

---

# 📈 Experimental Results

The developed framework demonstrates improvements in

- Intrusion Detection
- Trust Computation
- Secure Routing
- Blockchain Verification
- Overall Network Reliability

Generated result files include

```
results/

├── blockchain.json
├── final_results.csv
├── metrics.csv
└── xgboost_metrics.csv
```

Additional trained artifacts

```
outputs/models/

├── xgboost.pkl
└── xgb_features.pkl
```

---

# 🖥 Dashboard

The Streamlit dashboard provides complete visualization of

- Network Topology
- Trust Analytics
- Blockchain Ledger
- XGBoost Predictions
- Performance Comparison
- Evaluation Metrics
- Engine Comparison
- Overall System Overview

---

# 📸 Dashboard Screenshots

## Overall Dashboard

![Overview](SS/overview.png.png)

---

## Trust Analytics

![Network Trust](SS/networkTrust.png.png)

---

## XGBoost Intrusion Detection

![XGBoost](SS/xgBoost.png.png)

---

## Engine Comparison

![Engine Comparison](SS/engineComparision.png.png)

---

# 🚀 Future Improvements

Potential future enhancements include

- Deep Learning based Intrusion Detection
- Graph Neural Networks for Trust Prediction
- Federated Learning
- Online Incremental Learning
- Real-Time Packet Capture Integration
- IoT Sensor Deployment
- SDN Integration
- Edge AI Deployment
- Explainable AI (XAI)
- Kubernetes Deployment
- Cloud-based Distributed Monitoring
- Digital Twin Integration

---

# 📚 References

This project is inspired by recent research in

- Blockchain-enabled Trust Management
- Wireless Sensor Networks
- Machine Learning based Intrusion Detection
- XGBoost Classification
- Proof of Trust Consensus
- AdRS-MPIQ Secure Routing Framework

The routing and trust concepts are adapted and experimentally extended based on the AdRS-MPIQ secure routing framework presented in recent WSN research.

---

# 👩‍💻 Author

**Prateeksha Bhat**

Computer Science Engineering

Artificial Intelligence • Machine Learning • Cybersecurity • Blockchain • Network Security • Full Stack Development

GitHub

https://github.com/prateeksha-bhat-2508

---

