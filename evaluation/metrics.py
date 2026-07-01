from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)


class Evaluation:

    def __init__(self, df):
        self.df = df.copy()

    def compute(self, score_column, threshold=None):

        # Use adaptive threshold
        if threshold is None:
            threshold = self.df[score_column].mean()

        y_true = self.df["Attack_Probability"] > 0.5
        y_pred = self.df[score_column] < threshold

        accuracy = accuracy_score(y_true, y_pred)

        precision = precision_score(
            y_true,
            y_pred,
            zero_division=0
        )

        recall = recall_score(
            y_true,
            y_pred,
            zero_division=0
        )

        f1 = f1_score(
            y_true,
            y_pred,
            zero_division=0
        )

        tn, fp, fn, tp = confusion_matrix(
            y_true,
            y_pred,
            labels=[False, True]
        ).ravel()

        detection_rate = recall

        false_positive_rate = (
            fp / (fp + tn)
            if (fp + tn) > 0 else 0
        )

        trust_stability = max(
            0,
            1 - self.df[score_column].std()
        )

        validator_reliability = self.df["Consensus"].iloc[0]

        return {

            "Accuracy": accuracy,

            "Precision": precision,

            "Recall": recall,

            "F1-Score": f1,

            "Detection Rate": detection_rate,

            "False Positive Rate": false_positive_rate,

            "Trust Stability": trust_stability,

            "Validator Reliability": validator_reliability

        }