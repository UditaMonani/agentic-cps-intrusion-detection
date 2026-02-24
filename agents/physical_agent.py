import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os
import config
from utils.logger import get_logger

logger = get_logger("PhysicalAgent")

class PhysicalAgent:
    def __init__(self):
        self.model = IsolationForest(contamination=0.05, random_state=42)
        self.features = config.PHYSICAL_FEATURES
        self.model_path = config.PHYSICAL_MODEL_PATH

    def train(self, data_path):
        logger.info("Training Physical Agent on normal data...")
        df = pd.read_csv(data_path)
        X = df[self.features].values
        self.model.fit(X)
        joblib.dump(self.model, self.model_path)
        logger.info("Physical Agent training complete and model saved.")

    def load_model(self):
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
        else:
            raise FileNotFoundError("Physical model not found. Train first.")

    def detect(self, df):
        X = df[self.features].values
        # Sklearn returns negative values for anomalies. We invert it so higher = anomalous.
        scores = -self.model.decision_function(X)
        return scores