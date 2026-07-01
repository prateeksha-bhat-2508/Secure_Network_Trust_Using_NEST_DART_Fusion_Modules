import joblib
import pandas as pd

model = joblib.load("outputs/models/xgboost.pkl")


def predict_attack_probability(df):

    X = pd.DataFrame()

    X["Flow Duration"] = df["duration"]

    X["Total Fwd Packets"] = df["src_pkts"]

    X["Total Backward Packets"] = df["dst_pkts"]

    X["Total Length of Fwd Packets"] = df["src_bytes"]

    X["Total Length of Bwd Packets"] = df["dst_bytes"]

    return model.predict_proba(X)[:, 1]