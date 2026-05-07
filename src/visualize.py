import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_anomalies():
    # Load the results from our model script
    # (Ensure you run src/data_gen.py and src/model.py first!)
    try:
        df = pd.read_csv("data/synthetic_auth_logs.csv")
        # For visualization, let's simulate the 'anomaly' column if model.py wasn't run as a module
        from model import detect_anomalies
        # Assuming you've modified model.py to return the dataframe:
    except:
        print("Please run data_gen.py and model.py first.")
        return

    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='failed_attempts', y='session_duration', 
                    hue='anomaly', palette={1: 'blue', -1: 'red'})
    
    plt.title("Authentication Anomaly Detection (Isolation Forest)")
    plt.xlabel("Failed Login Attempts")
    plt.ylabel("Session Duration (Seconds)")
    plt.legend(title='Is Anomaly?', labels=['Normal', 'Anomaly'])
    plt.show()

if __name__ == "__main__":
    # If you haven't run the model yet, this might fail. 
    # Let's keep it simple for now.
    print("Visualization script ready. Run this after generating the 'anomaly' column.")