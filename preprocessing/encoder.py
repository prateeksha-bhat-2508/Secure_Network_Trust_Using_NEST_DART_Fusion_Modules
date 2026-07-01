import pandas as pd
from sklearn.preprocessing import LabelEncoder
from utils.logger import logger


class DataEncoder:

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.encoders = {}

    def encode(self):

        categorical = self.df.select_dtypes(include=["object"]).columns

        categorical = [
            c for c in categorical
            if c not in ["src_ip", "dst_ip"]
        ]

        exclude = [
            "src_ip",
            "dst_ip"
        ]

        categorical = [
            col for col in categorical
            if col not in exclude
        ]


        for col in categorical:

            encoder = LabelEncoder()

            self.df[col] = encoder.fit_transform(
                self.df[col].astype(str)
            )

            self.encoders[col] = encoder

            logger.info(f"Encoded {col}")

        return self.df