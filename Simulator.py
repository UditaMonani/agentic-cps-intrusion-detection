import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
import json
import time
import random

# Connect to the same broker as your AgenticEngine
client = mqtt.Client(CallbackAPIVersion.VERSION2, "Grid_Simulator")
client.connect("broker.hivemq.com", 1883)

print("🚀 Starting Grid Simulation...")

try:
    while True:
        # Phase 1: Normal Operation
        for _ in range(10):
            data = {
                "packet_rate": random.uniform(10, 20),
                "voltage": random.uniform(0.98, 1.02)
            }
            client.publish("grid/sensors", json.dumps(data))
            print(f"✅ Normal Data Sent: {data}")
            time.sleep(1)

        # Phase 2: Coordinated Attack (MadIoT)
        print("⚠️ TRIGGERING ATTACK...")
        for _ in range(5):
            data = {
                "packet_rate": random.uniform(100, 150), # Cyber Spike
                "voltage": random.uniform(0.85, 0.90)    # Physical Drop
            }
            client.publish("grid/sensors", json.dumps(data))
            print(f"🚨 ATTACK Data Sent: {data}")
            time.sleep(1)
            
except KeyboardInterrupt:
    print("Simulation Stopped.")