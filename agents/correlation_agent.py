import config
from utils.logger import get_logger

logger = get_logger("CorrelationAgent")

class CorrelationAgent:
    def __init__(self):
        self.threshold = config.ANOMALY_THRESHOLD

    def correlate(self, network_score, physical_score):
        """Rule-based inference to attribute the anomaly."""
        net_anom = network_score > self.threshold
        phys_anom = physical_score > self.threshold

        if net_anom and phys_anom:
            return "Coordinated Cyber-Physical Attack"
        elif phys_anom and not net_anom:
            return "Mechanical Fault or Sensor Fault"
        elif net_anom and not phys_anom:
            return "External Cyber Intrusion Attempt"
        else:
            return "Normal Operations"