import paho.mqtt.client as mqtt
import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
import json
import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion  
from agents.network_agent import NetworkAgent 
from agents.physical_agent import PhysicalAgent

# Setup Isolation Forests with "Historical" baseline
# In production, you'd load a pre-trained .pkl file here
net_agent = IsolationForest(contamination=0.05).fit(np.random.randn(100, 1))
phys_agent = IsolationForest(contamination=0.05).fit(np.random.randn(100, 1))

def on_message(client, userdata, message):
    data = json.loads(message.payload)
    
    # 1. Extract real-time features
    net_val = np.array([[data['packet_rate']]])
    phys_val = np.array([[data['voltage']]])
    
    # 2. Agents calculate Anomaly Scores
    net_score = -net_agent.decision_function(net_val)[0]
    phys_score = -phys_agent.decision_function(phys_val)[0]
    
    # 3. Correlation Logic (The Handshake)
    is_attack = "NORMAL"
    if net_score > 0 and phys_score > 0:
        is_attack = "COORDINATED ATTACK"
    elif net_score > 0:
        is_attack = "CYBER BREACH"
        
    print(f"Status: {is_attack} | Net: {net_score:.2f} | Phys: {phys_score:.2f}")

# MQTT Setup
client = mqtt.Client(CallbackAPIVersion.VERSION2, "CPS_Sentinel") 

# client.connect("localhost", 1883)
client.connect("broker.hivemq.com", 1883)
client.subscribe("grid/sensors")
client.on_message = on_message

print("Agentic Engine is running and listening for data...")
client.loop_forever()