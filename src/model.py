import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

def detect_anomalies():
    # 1. Load the data
    df = pd.read_csv("data/synthetic_auth_logs.csv")
    
    # 2. Feature Engineering
    # We only use numerical features for the basic model
    features = ['failed_attempts', 'session_duration']
    X = df[features]
    
    # 3. Scaling the data (crucial for distance-based and tree-based algorithms)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # 4. Train the Isolation Forest
    # contamination defines the proportion of outliers we expect in the data
    model = IsolationForest(contamination=0.01, random_state=42)
    model.fit(X_scaled)
    
    # 5. Predict (-1 indicates an anomaly, 1 indicates normal)
    df['anomaly'] = model.predict(X_scaled)
    
    # 6. Review Results
    anomalies = df[df['anomaly'] == -1]
    
    print(f"Total records analyzed: {len(df)}")
    print(f"Anomalies detected: {len(anomalies)}")
    print("\nSample of detected anomalies:")
    print(anomalies[['user_id', 'failed_attempts', 'session_duration']].head(10))

if __name__ == "__main__":
    detect_anomalies()
