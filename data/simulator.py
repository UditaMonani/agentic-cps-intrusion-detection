import pandas as pd
import numpy as np
import os
import config

def generate_normal_data():
    """Generates synthetic normal time-series data for sensors and network logs."""
    np.random.seed(42)
    n = config.NUM_SAMPLES
    
    # Physical sensor data (DM Water Cooling System)
    chlorine = np.random.normal(loc=1.5, scale=0.1, size=n)
    flow = np.random.normal(loc=100.0, scale=2.0, size=n)
    temp = np.random.normal(loc=30.0, scale=0.5, size=n)
    ph = np.random.normal(loc=7.2, scale=0.05, size=n)
    
    # Network logs
    packet_rate = np.random.normal(loc=500.0, scale=20.0, size=n)
    connections = np.random.normal(loc=50.0, scale=5.0, size=n).astype(int)
    failed_logins = np.random.poisson(lam=0.1, size=n)
    
    df = pd.DataFrame({
        "timestamp": pd.date_range(start="2026-02-23 00:00:00", periods=n, freq="s"),
        "chlorine_level": chlorine,
        "flow_rate": flow,
        "temperature": temp,
        "pH": ph,
        "packet_rate": packet_rate,
        "connections": connections,
        "failed_logins": failed_logins
    })
    
    df.to_csv(config.NORMAL_DATA_PATH, index=False)
    return df