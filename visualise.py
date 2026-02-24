import pandas as pd
import matplotlib.pyplot as plt
import config
from agents.network_agent import NetworkAgent
from agents.physical_agent import PhysicalAgent

def run_visualization():
    # Load data
    df = pd.read_csv(config.ATTACK_DATA_PATH)
    
    # Get scores
    net_agent = NetworkAgent()
    phys_agent = PhysicalAgent()
    net_agent.load_model()
    phys_agent.load_model()
    
    net_scores = net_agent.detect(df)
    phys_scores = phys_agent.detect(df)

    # Plotting
    fig, ax = plt.subplots(3, 1, figsize=(12, 10), sharex=True)
    
    # 1. Physical Attack Evidence
    ax[0].plot(df.index, df['chlorine_level'], color='green', label='Chlorine Level')
    ax[0].set_title("Physical Process: Chlorine Levels (Spike Detected)")
    ax[0].axvspan(config.ATTACK_START, config.ATTACK_END, color='red', alpha=0.2, label='Attack Window')
    ax[0].legend()

    # 2. Cyber Attack Evidence
    ax[1].plot(df.index, df['packet_rate'], color='blue', label='Packet Rate')
    ax[1].set_title("Network Traffic: Packet Rate (Burst Detected)")
    ax[1].axvspan(config.ATTACK_START, config.ATTACK_END, color='red', alpha=0.2)
    ax[1].legend()

    # 3. Agent Anomaly Scores
    ax[2].plot(df.index, net_scores, label='Network Anomaly Score', alpha=0.7)
    ax[2].plot(df.index, phys_scores, label='Physical Anomaly Score', alpha=0.7)
    ax[2].axhline(y=config.ANOMALY_THRESHOLD, color='black', linestyle='--', label='Threshold')
    ax[2].set_title("Multi-Agent Anomaly Detection Scores")
    ax[2].legend()

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    run_visualization()