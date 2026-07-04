import joblib
import pandas as pd

class XGBoostIDS:
    """
    A simple wrapper around the XGBoost model.
    It loads the model and feature list, and provides prediction methods.
    """
    def __init__(self, model_path="outputs/models/xgboost.pkl",
                 features_path="outputs/models/xgb_features.pkl"):
        self.model = joblib.load(model_path)
        self.features = joblib.load(features_path)

    def predict(self, X):
        """Return binary predictions (0/1) for input DataFrame."""
        return self.model.predict(X[self.features])

    def predict_probability(self, X):
        """Return attack probabilities (0..1) for input DataFrame."""
        return self.model.predict_proba(X[self.features])[:, 1]