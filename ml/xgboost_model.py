import joblib

MODEL_PATH = "outputs/models/xgboost.pkl"

class XGBoostIDS:

    def __init__(self):
        self.model = joblib.load(MODEL_PATH)

    def predict(self, X):
        return self.model.predict(X)

    def predict_probability(self, X):
        return self.model.predict_proba(X)[:, 1]