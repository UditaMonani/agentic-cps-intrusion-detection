import os
import config
from data.simulator import generate_normal_data
from data.attack_injector import inject_attack
from agents.network_agent import NetworkAgent
from agents.physical_agent import PhysicalAgent
from agents.correlation_agent import CorrelationAgent
from utils.logger import get_logger
import pandas as pd

logger = get_logger("MainOrchestrator")

def setup_directories():
    os.makedirs(config.DATA_DIR, exist_ok=True)
    os.makedirs(config.MODELS_DIR, exist_ok=True)

def main():
    setup_directories()
    
    # 1. Simulate Normal Data
    logger.info("--- Phase 1: Data Simulation ---")
    generate_normal_data()
    logger.info("Normal baseline data generated.")
    
    # 2. Inject Attack Scenarios
    logger.info("--- Phase 2: Attack Injection ---")
    inject_attack()
    logger.info("Attack scenarios injected into test set.")
    
    # 3. Initialize and Train Agents
    logger.info("--- Phase 3: Agent Training ---")
    net_agent = NetworkAgent()
    phys_agent = PhysicalAgent()
    
    net_agent.train(config.NORMAL_DATA_PATH)
    phys_agent.train(config.NORMAL_DATA_PATH)
    
    # Load trained models
    net_agent.load_model()
    phys_agent.load_model()
    
    # 4. Detect Anomalies on Injected Data
    logger.info("--- Phase 4: Real-time Detection ---")
    attack_df = pd.read_csv(config.ATTACK_DATA_PATH)
    
    net_scores = net_agent.detect(attack_df)
    phys_scores = phys_agent.detect(attack_df)
    
    # 5. Correlate and Evaluate Output
    logger.info("--- Phase 5: Correlation & Attribution ---")
    corr_agent = CorrelationAgent()
    
    # Select a specific time step deep inside the attack window (e.g., index 825)
    test_index = config.ATTACK_START + 25 
    
    target_net_score = round(net_scores[test_index], 4)
    target_phys_score = round(phys_scores[test_index], 4)
    
    final_decision = corr_agent.correlate(target_net_score, target_phys_score)
    
    # 6. Final Evaluation Printout
    print("\n" + "="*40)
    print("EVALUATION AT TIMESTEP:", test_index)
    print("="*40)
    print("-" * 25)
    print(f"Network Anomaly Score: {target_net_score}")
    print(f"Physical Anomaly Score: {target_phys_score}")
    print(f"Final Attribution: {final_decision}")
    print("-" * 25)

if __name__ == "__main__":
    main()