AI-Driven Threat Detection System

Anomaly Detection in Network Traffic using Machine Learning

This project implements an AI-powered threat detection system that analyzes network traffic to identify potential cyber threats and anomalies.
It applies machine learning (Isolation Forest) to distinguish between normal and malicious activity patterns, simulating real-world detection pipelines used in Security Operations Centers (SOC) and threat intelligence research (Microsoft MSTIC-style).

Project Structure :
File	Description
ai_threat_detection.py : Main script — trains and tests the anomaly detection model on synthetic traffic data.
generate_synthetic_network_data.py : Generates synthetic network traffic datasets (normal + abnormal samples).
generate_synthetic_traffic.py : Simulates network packets and exports them as a .pcap capture for further analysis.

Prerequisites :
Python: 3.x
Required libraries:

pip install numpy pandas scikit-learn scapy

How to Run it :
1. Generate Synthetic Network Traffic Data
python generate_synthetic_network_data.py


Creates synthetic_network_data.csv with both normal and malicious traffic samples.

2. Train and Evaluate the Detection Model
python ai_threat_detection.py


Trains an Isolation Forest model and outputs accuracy, detection rate, and confusion matrix.
Results include:

Precision / recall / F1-score

Visualization of anomalies vs. normal traffic

3. Generate Synthetic Network Packets
python generate_synthetic_traffic.py


Creates a .pcap file containing simulated TCP/IP packets (normal + attack patterns).
Can be inspected using Wireshark or Zeek.

Project Overview :
ai_threat_detection.py
- Loads and preprocesses synthetic network traffic data
- Trains an Isolation Forest model to identify anomalies
- Evaluates predictions and produces a report

generate_synthetic_network_data.py
- Creates realistic features (packet size, source/destination ports, time delta, protocol)
- Mixes normal and abnormal behaviors (e.g., port scans, brute-force bursts)
- Exports dataset as CSV

generate_synthetic_traffic.py
- Uses Scapy to create and store packet captures
- Simulates random IPs, port scans, SYN floods

Use Case of this project

This project serves as a proof-of-concept for AI-based intrusion detection, bridging:

Machine learning in cybersecurity
Threat hunting and network telemetry
Data analysis for anomaly detection
Ideal as a foundation for advanced research in:
Threat Intelligence (TI)
Cloud Security Analytics
SIEM / SOC Automation

References

Microsoft Threat Intelligence Center (MSTIC) Research Methodologies
Scikit-Learn Documentation: https://scikit-learn.org/stable/
Scapy Packet Manipulation: https://scapy.readthedocs.io/