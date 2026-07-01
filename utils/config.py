from pathlib import Path

# =====================================================
# PROJECT ROOT
# =====================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent

# =====================================================
# DATASET DIRECTORIES
# =====================================================

DATASET_DIR = PROJECT_ROOT / "datasets"

NETWORK_DIR = DATASET_DIR / "network"
IOT_DIR = DATASET_DIR / "iot"
PROCESSED_DIR = DATASET_DIR / "processed"

# =====================================================
# NETWORK DATASETS
# =====================================================

NETWORK_DATASET = NETWORK_DIR / "train_test_network.csv"

UNSW_TRAIN = NETWORK_DIR / "UNSW_NB15_training-set.csv"

UNSW_TEST = NETWORK_DIR / "UNSW_NB15_testing-set.csv"

# =====================================================
# IOT DATASETS
# =====================================================

IOT_FRIDGE = IOT_DIR / "Train_Test_IoT_Fridge.csv"

IOT_GARAGE = IOT_DIR / "Train_Test_IoT_Garage_Door.csv"

IOT_GPS = IOT_DIR / "Train_Test_IoT_GPS_Tracker.csv"

IOT_MODBUS = IOT_DIR / "Train_Test_IoT_Modbus.csv"

IOT_MOTION = IOT_DIR / "Train_Test_IoT_Motion_Light.csv"

IOT_THERMOSTAT = IOT_DIR / "Train_Test_IoT_Thermostat.csv"

IOT_WEATHER = IOT_DIR / "Train_Test_IoT_Weather.csv"

# =====================================================
# OUTPUT DIRECTORIES
# =====================================================

OUTPUT_DIR = PROJECT_ROOT / "outputs"

MODEL_DIR = OUTPUT_DIR / "models"

GRAPH_DIR = OUTPUT_DIR / "graphs"

REPORT_DIR = OUTPUT_DIR / "reports"

LOG_DIR = OUTPUT_DIR / "logs"

# =====================================================
# RANDOM SEED
# =====================================================

RANDOM_STATE = 42