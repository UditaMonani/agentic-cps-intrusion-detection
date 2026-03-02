import streamlit as st
import pandas as pd
import time
import numpy as np

st.set_page_config(page_title="GridGuard Command Center", layout="wide")

st.title("⚡ GridGuard: Agentic CPS Sentinel")
st.subheader("Real-Time Distribution Grid Monitoring")

# Sidebar for System Health
st.sidebar.header("System Status")
st.sidebar.success("Network Agent: ACTIVE")
st.sidebar.success("Physical Agent: ACTIVE")

# Create Placeholders for live data
col1, col2 = st.columns(2)
with col1:
    st.write("### Network Traffic (Packets/s)")
    net_chart = st.line_chart(np.zeros((20,1)))
with col2:
    st.write("### Physical Voltage (pu)")
    phys_chart = st.line_chart(np.zeros((20,1)))

# The "Big Red Button" Alert
alert_placeholder = st.empty()

# Simulation Loop for Dashboard
# In production, this would read from a Database (like InfluxDB)
for i in range(100):
    # Mocking real-time feed
    val = np.random.randn()
    net_chart.add_rows([val])
    phys_chart.add_rows([val * 0.5])
    
    if val > 2:
        alert_placeholder.error("🚨 CRITICAL: COORDINATED ATTACK DETECTED")
    else:
        alert_placeholder.info("✅ System Status: Secure")
        
    time.sleep(0.5)