import pandas as pd
import numpy as np
import config

def inject_attack():
    """Injects a coordinated cyber-physical attack into the normal data."""
    df = pd.read_csv(config.NORMAL_DATA_PATH)
    
    start = config.ATTACK_START
    end = config.ATTACK_END
    
    # 1. Physical Attack Injection: Chlorine spike and flow drop
    df.loc[start:end, "chlorine_level"] += np.random.uniform(2.0, 3.0, size=end-start+1)
    df.loc[start:end, "flow_rate"] -= np.random.uniform(40.0, 50.0, size=end-start+1)
    
    # 2. Cyber Attack Injection: Packet burst and external IP spike (failed logins)
    df.loc[start:end, "packet_rate"] += np.random.uniform(1000.0, 1500.0, size=end-start+1)
    df.loc[start:end, "failed_logins"] += np.random.poisson(lam=15, size=end-start+1)
    
    df.to_csv(config.ATTACK_DATA_PATH, index=False)
    return df