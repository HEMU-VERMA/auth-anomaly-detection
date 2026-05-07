# Authentication Anomaly Detection System 🛡️

## Overview
This project demonstrates the application of Unsupervised Machine Learning to cybersecurity. By utilizing an Isolation Forest algorithm, this system identifies anomalous authentication behaviors—such as brute force attempts or suspicious bot activity—from standard server login logs.

## The Problem
Traditional rule-based security systems often fail to detect sophisticated, low-and-slow attacks or unusual behavioral patterns that don't trigger hardcoded thresholds. Machine learning provides a dynamic way to flag irregularities by learning the baseline of normal user behavior and isolating the outliers.

## Tech Stack
* **Language:** Python
* **Data Processing:** Pandas, NumPy
* **Machine Learning:** Scikit-Learn (Isolation Forest, StandardScaler)
* **Visualization:** Matplotlib, Seaborn

## Project Structure

auth-anomaly-detection/

├── data/
│   └── synthetic_auth_logs.csv   # Generated dataset
├── notebooks/                    # Jupyter notebooks for EDA (optional)
├── src/
│   ├── data_gen.py               # Script to generate logs with injected attacks
│   ├── model.py                  # Isolation Forest detection logic
│   └── visualize.py              # Visualizing anomalies via scatter plots
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
