import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_auth_logs(num_records=5000):
    np.random.seed(42)
    
    # Normal user behavior parameters
    users = [f"user_{i}" for i in range(1, 101)]
    locations = ["US", "UK", "IN", "CA", "DE"]
    
    data = []
    start_time = datetime(2026, 5, 1)
    
    for _ in range(num_records):
        user = random.choice(users)
        timestamp = start_time + timedelta(minutes=random.randint(1, 43200))
        failed_attempts = np.random.choice([0, 1, 2], p=[0.85, 0.10, 0.05])
        session_duration = int(np.random.normal(300, 50)) # Normal session ~5 mins
        location = random.choice(locations)
        
        data.append([user, timestamp, failed_attempts, session_duration, location])

    df = pd.DataFrame(data, columns=["user_id", "timestamp", "failed_attempts", "session_duration", "location"])
    
    # Injecting Anomalies (The "Attacks")
    # Anomaly 1: Brute force (High failed attempts)
    for _ in range(20):
        df.loc[random.randint(0, num_records-1), 'failed_attempts'] = random.randint(15, 50)
        
    # Anomaly 2: Bot behavior (Extremely short sessions)
    for _ in range(20):
        df.loc[random.randint(0, num_records-1), 'session_duration'] = random.randint(1, 5)

    df.to_csv("data/synthetic_auth_logs.csv", index=False)
    print("Synthetic data generated and saved to data/synthetic_auth_logs.csv")

if __name__ == "__main__":
    generate_auth_logs()