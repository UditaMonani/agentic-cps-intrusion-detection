import os

# Base paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODELS_DIR = os.path.join(BASE_DIR, "models")

# File paths
NORMAL_DATA_PATH = os.path.join(DATA_DIR, "normal_data.csv")
ATTACK_DATA_PATH = os.path.join(DATA_DIR, "attack_data.csv")
NETWORK_MODEL_PATH = os.path.join(MODELS_DIR, "network_model.pkl")
PHYSICAL_MODEL_PATH = os.path.join(MODELS_DIR, "physical_model.pkl")

# Simulation parameters
NUM_SAMPLES = 1000
ATTACK_START = 800
ATTACK_END = 850

# Features
PHYSICAL_FEATURES = ["chlorine_level", "flow_rate", "temperature", "pH"]
NETWORK_FEATURES = ["packet_rate", "connections", "failed_logins"]

# Thresholds (Anomaly scores > threshold are flagged)
# Note: Inverted IsolationForest decision_function so higher is more anomalous.
ANOMALY_THRESHOLD = 0.05