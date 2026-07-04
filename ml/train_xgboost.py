import os
import glob
import joblib
import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, roc_auc_score, confusion_matrix
)

# ============================================================
# CONFIGURATION
# ============================================================

# Point this to your dataset CSV file (or folder containing CSVs)
DATASET_PATH = "datasets/network/train_test_network.csv"   # <--- CHANGE THIS

# Alternatively, if you have multiple CSV files in a folder:
# DATASET_PATH = "datasets/MachineLearningCVE/*.csv"

# Features to use (must match columns in the dataset)
FEATURES = [
    "duration",
    "src_pkts",
    "dst_pkts",
    "src_bytes",
    "dst_bytes"
]

LABEL_COL = "label"          # 0 = benign, 1 = attack
TEST_SIZE = 0.2
RANDOM_STATE = 42

# XGBoost hyperparameters (same as your original)
XGB_PARAMS = {
    "n_estimators": 300,
    "max_depth": 8,
    "learning_rate": 0.05,
    "subsample": 0.8,
    "colsample_bytree": 0.8,
    "random_state": RANDOM_STATE,
    "eval_metric": "logloss",
    "tree_method": "hist"
}

# ============================================================
# LOAD DATA
# ============================================================

def load_data(path):
    """Load a single CSV or all CSVs in a folder."""
    if os.path.isdir(path):
        csv_files = glob.glob(os.path.join(path, "*.csv"))
        print(f"Found {len(csv_files)} CSV files in {path}")
        dfs = []
        for f in csv_files:
            print(f"  Loading {os.path.basename(f)} ...")
            dfs.append(pd.read_csv(f, low_memory=False))
        return pd.concat(dfs, ignore_index=True)
    else:
        print(f"Loading single CSV: {path}")
        return pd.read_csv(path, low_memory=False)

df = load_data(DATASET_PATH)
print(f"Initial shape: {df.shape}")

# Strip column names
df.columns = df.columns.str.strip()

# ============================================================
# CLEAN DATA
# ============================================================

# Drop duplicates
df.drop_duplicates(inplace=True)

# Replace infinities with NaN
df.replace([np.inf, -np.inf], np.nan, inplace=True)

# Ensure label is integer
if LABEL_COL not in df.columns:
    raise KeyError(f"Label column '{LABEL_COL}' not found.")
df[LABEL_COL] = df[LABEL_COL].astype(int)

# Keep only the required features + label
required_cols = FEATURES + [LABEL_COL]
missing = [c for c in required_cols if c not in df.columns]
if missing:
    raise ValueError(f"Missing columns: {missing}")

df = df[required_cols].copy()

# Drop rows with NaN (if any)
df.dropna(inplace=True)
print(f"After cleaning: {df.shape}")

# ============================================================
# SPLIT FEATURES / TARGET
# ============================================================

X = df[FEATURES]
y = df[LABEL_COL]

# Check class distribution
print("Class distribution:")
print(y.value_counts())

# If you only have one class, training will fail – warn the user
if len(y.unique()) < 2:
    print("WARNING: Only one class present. Model will be useless.")
    # You might want to exit or handle differently

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=TEST_SIZE,
    random_state=RANDOM_STATE,
    stratify=y
)

print(f"Training samples: {len(X_train)}")
print(f"Testing samples : {len(X_test)}")

# ============================================================
# TRAIN XGBOOST
# ============================================================

model = XGBClassifier(**XGB_PARAMS)
print("\nTraining XGBoost...")
model.fit(X_train, y_train)

# ============================================================
# EVALUATE
# ============================================================

y_pred = model.predict(X_test)
y_proba = model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, zero_division=0)
recall = recall_score(y_test, y_pred, zero_division=0)
f1 = f1_score(y_test, y_pred, zero_division=0)
roc = roc_auc_score(y_test, y_proba)
tn, fp, fn, tp = confusion_matrix(y_test, y_pred).ravel()
detection_rate = tp / (tp + fn) if (tp + fn) > 0 else 0
false_positive_rate = fp / (fp + tn) if (fp + tn) > 0 else 0

print("\n" + "="*50)
print("XGBOOST EVALUATION")
print("="*50)
print(f"Accuracy       : {accuracy:.4f}")
print(f"Precision      : {precision:.4f}")
print(f"Recall         : {recall:.4f}")
print(f"F1-score       : {f1:.4f}")
print(f"ROC AUC        : {roc:.4f}")
print(f"Detection Rate : {detection_rate:.4f}")
print(f"False Positive Rate : {false_positive_rate:.4f}")

# ============================================================
# SAVE MODEL & FEATURES
# ============================================================

os.makedirs("outputs/models", exist_ok=True)
joblib.dump(model, "outputs/models/xgboost.pkl")
joblib.dump(FEATURES, "outputs/models/xgb_features.pkl")
print("\nModel and feature list saved to outputs/models/")

# Save metrics to CSV
os.makedirs("results", exist_ok=True)
metrics_df = pd.DataFrame({
    "Metric": ["Accuracy", "Precision", "Recall", "F1-Score", "ROC-AUC",
               "Detection Rate", "False Positive Rate"],
    "Value": [accuracy, precision, recall, f1, roc, detection_rate, false_positive_rate]
})
metrics_df.to_csv("results/xgboost_metrics.csv", index=False)
print("Metrics saved to results/xgboost_metrics.csv")