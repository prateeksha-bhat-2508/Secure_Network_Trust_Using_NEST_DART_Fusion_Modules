import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from utils.logger import logger


class DataScaler:

    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()

    def scale(self):

        numeric = self.df.select_dtypes(include=["number"]).columns

        exclude = [
            "src_ip",
            "dst_ip"
        ]

        numeric = [
            col for col in numeric
            if col not in exclude
        ]

        scaler = MinMaxScaler()

        self.df[numeric] = scaler.fit_transform(
            self.df[numeric]
        )

        logger.info("Scaling completed.")

        return self.df