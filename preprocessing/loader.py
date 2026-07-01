import pandas as pd
from pathlib import Path
from typing import Dict

from utils.config import (
    NETWORK_DATASET,
    UNSW_TRAIN,
    UNSW_TEST,
    IOT_FRIDGE,
    IOT_GARAGE,
    IOT_GPS,
    IOT_MODBUS,
    IOT_MOTION,
    IOT_THERMOSTAT,
    IOT_WEATHER
)

from utils.logger import logger


class DatasetLoader:

    def __init__(self):

        self.datasets = {
            "Network": NETWORK_DATASET,
            "UNSW_Train": UNSW_TRAIN,
            "UNSW_Test": UNSW_TEST,
            "Fridge": IOT_FRIDGE,
            "Garage_Door": IOT_GARAGE,
            "GPS_Tracker": IOT_GPS,
            "Modbus": IOT_MODBUS,
            "Motion_Light": IOT_MOTION,
            "Thermostat": IOT_THERMOSTAT,
            "Weather": IOT_WEATHER
        }

    def verify_datasets(self):

        logger.info("Checking dataset availability...")

        for name, path in self.datasets.items():

            if Path(path).exists():
                logger.info(f"{name} FOUND")
            else:
                logger.error(f"{name} NOT FOUND -> {path}")

    def load_dataset(self, name: str) -> pd.DataFrame:

        if name not in self.datasets:
            raise ValueError(f"{name} dataset not found.")

        logger.info(f"Loading {name} dataset...")

        df = pd.read_csv(self.datasets[name])

        logger.info(
            f"{name}: {df.shape[0]} rows × {df.shape[1]} columns"
        )

        return df

    def load_all(self) -> Dict[str, pd.DataFrame]:

        data = {}

        for name in self.datasets:

            try:
                data[name] = self.load_dataset(name)

            except Exception as e:

                logger.error(f"{name}: {e}")

        return data

    def dataset_summary(self, df: pd.DataFrame):

        print("\nShape")
        print(df.shape)

        print("\nColumns")
        print(df.columns.tolist())

        print("\nMissing Values")
        print(df.isnull().sum())

        print("\nData Types")
        print(df.dtypes)

        print("\nFirst Five Rows")
        print(df.head())

    def get_iot_datasets(self):

        iot = {}

        for name in [
            "Fridge",
            "Garage_Door",
            "GPS_Tracker",
            "Modbus",
            "Motion_Light",
            "Thermostat",
            "Weather"
        ]:

            iot[name] = self.load_dataset(name)

        return iot

    def get_network_datasets(self):

        network = {}

        for name in [
            "Network",
            "UNSW_Train",
            "UNSW_Test"
        ]:

            network[name] = self.load_dataset(name)

        return network