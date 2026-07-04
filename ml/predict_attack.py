import joblib
import pandas as pd

# Load model once at module import
MODEL_PATH = "outputs/models/xgboost.pkl"
FEATURES_PATH = "outputs/models/xgb_features.pkl"

_model = None
_features = None

def _load_model():
    global _model, _features
    if _model is None:
        _model = joblib.load(MODEL_PATH)
        _features = joblib.load(FEATURES_PATH)
    return _model, _features

def predict_attack_probability(df):
    """
    Predict attack probability for each row in the given DataFrame.
    Expects the following columns:
        duration, src_pkts, dst_pkts, src_bytes, dst_bytes
    Returns a numpy array of probabilities (0..1).
    """
    model, features = _load_model()

    # Build feature matrix from the required columns
    X = pd.DataFrame()
    # Map to the exact feature names used during training
    # (The model was trained with these five columns)
    for col in features:
        if col not in df.columns:
            raise ValueError(f"Missing required column: {col}")
        X[col] = df[col]

    # Ensure numeric, fill NaNs if any (just in case)
    X = X.astype(float).fillna(0)

    return model.predict_proba(X)[:, 1]