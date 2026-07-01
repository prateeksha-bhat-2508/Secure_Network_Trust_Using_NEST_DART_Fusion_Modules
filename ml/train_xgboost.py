import os
import glob
import joblib
import pandas as pd
import numpy as np

from xgboost import XGBClassifier

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import LabelEncoder

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    roc_auc_score,
    confusion_matrix,
)

# ==========================================
# Dataset Folder
# ==========================================

DATASET_FOLDER = r"datasets/MachineLearningCVE"

# Change this to wherever you extracted the CSVs

# ==========================================
# Read all CSVs
# ==========================================

csv_files = glob.glob(
    os.path.join(DATASET_FOLDER, "*.csv")
)

print(f"\nFound {len(csv_files)} CSV files\n")

dfs = []

for file in csv_files:

    print("Loading:", os.path.basename(file))

    dfs.append(
        pd.read_csv(file, low_memory=False)
    )

df = pd.concat(
    dfs,
    ignore_index=True
)

print("\nTotal Shape:", df.shape)

print("\nCIC Columns:")
print(df.columns.tolist())

# ==========================================
# Clean Column Names
# ==========================================

df.columns = df.columns.str.strip()

# ==========================================
# Remove duplicates
# ==========================================

df.drop_duplicates(inplace=True)

# ==========================================
# Replace Inf
# ==========================================

df.replace(
    [np.inf, -np.inf],
    np.nan,
    inplace=True
)

df.dropna(inplace=True)

print("After Cleaning:", df.shape)

# ==========================================
# Label Column
# ==========================================

label_column = "Label"

# Binary classification

df[label_column] = np.where(
    df[label_column] == "BENIGN",
    0,
    1
)

# ==========================================
# Features
# ==========================================

COMMON_FEATURES = [
    "Destination Port",
    "Protocol",
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Total Length of Fwd Packets",
    "Total Length of Bwd Packets"
]

COMMON_FEATURES = [
    "Flow Duration",
    "Total Fwd Packets",
    "Total Backward Packets",
    "Total Fwd Packets",
    "Protocol",
    "Total Length of Fwd Packets",
    "Total Length of Bwd Packets"
]

X = df[COMMON_FEATURES]
y = df[label_column]

# ==========================================
# Encode categorical columns
# ==========================================

for col in X.select_dtypes(include="object").columns:

    encoder = LabelEncoder()

    X[col] = encoder.fit_transform(
        X[col].astype(str)
    )

# ==========================================
# Train Test Split
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(

    X,

    y,

    test_size=0.20,

    random_state=42,

    stratify=y

)

print("\nTraining Samples :", len(X_train))

print("Testing Samples :", len(X_test))

# ==========================================
# XGBoost
# ==========================================

model = XGBClassifier(

    n_estimators=300,

    max_depth=8,

    learning_rate=0.05,

    subsample=0.8,

    colsample_bytree=0.8,

    random_state=42,

    eval_metric="logloss",

    tree_method="hist"

)

print("\nTraining XGBoost...\n")

model.fit(

    X_train,

    y_train

)

# ==========================================
# Prediction
# ==========================================

prediction = model.predict(X_test)

probability = model.predict_proba(X_test)[:,1]

# ==========================================
# Metrics
# ==========================================

accuracy = accuracy_score(

    y_test,

    prediction

)

precision = precision_score(

    y_test,

    prediction

)

recall = recall_score(

    y_test,

    prediction

)

f1 = f1_score(

    y_test,

    prediction

)

roc = roc_auc_score(

    y_test,

    probability

)

tn,fp,fn,tp = confusion_matrix(

    y_test,

    prediction

).ravel()

print("\n==============================")

print("XGBOOST RESULTS")

print("==============================")

print("Accuracy :", accuracy)

print("Precision :", precision)

print("Recall :", recall)

print("F1 :", f1)

print("ROC AUC :", roc)

print("Detection Rate :", tp/(tp+fn))

print("False Positive Rate :", fp/(fp+tn))

# ==========================================
# Save Model
# ==========================================

os.makedirs(

    "outputs/models",

    exist_ok=True

)

joblib.dump(

    model,

    "outputs/models/xgboost.pkl"

)

print("\nModel Saved.")

metrics = pd.DataFrame({
    "Metric": [
        "Accuracy",
        "Precision",
        "Recall",
        "F1-Score",
        "ROC-AUC",
        "Detection Rate",
        "False Positive Rate"
    ],
    "Value": [
        accuracy,
        precision,
        recall,
        f1,
        roc,
        tp/(tp+fn),
        fp/(fp+tn)
    ]
})

os.makedirs("results", exist_ok=True)
metrics.to_csv("results/xgboost_metrics.csv", index=False)

print("Metrics Saved.")

joblib.dump(list(X.columns), "outputs/models/xgb_features.pkl")