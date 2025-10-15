# AI-Driven Threat Detection System

**Anomaly Detection in Network Traffic using Machine Learning**

This project implements an AI-powered threat detection system that analyzes network traffic to identify potential cyber threats and anomalies. It uses **Isolation Forest** to distinguish between normal and malicious activity patterns, simulating real-world detection pipelines used in **Security Operations Centers (SOC)** and threat intelligence research (Microsoft MSTIC-style).

---

## Project Structure

| File | Description |
|------|-------------|
| `src/ai_threat_detection.py` | Main script — trains and tests the anomaly detection model on synthetic traffic data. |
| `src/generate_synthetic_network_data.py` | Generates synthetic network traffic datasets (normal + abnormal samples). |
| `src/generate_synthetic_traffic.py` | Simulates network packets and exports them as a `.pcap` capture for analysis. |

---

## Prerequisites

- Python 3.x
- Create a virtual environment and activate it:
  - Windows: `venv\Scripts\activate`
  - macOS / Linux: `source venv/bin/activate`
- Install required libraries: `numpy`, `pandas`, `scikit-learn`, `scapy`

---

## How to Run

1. **Generate Synthetic Network Traffic Data**  
   Run `generate_synthetic_network_data.py` to create `data/synthetic_network_data.csv` containing normal and malicious traffic samples.

2. **Train and Evaluate the Detection Model**  
   Run `ai_threat_detection.py` to train an Isolation Forest model and output:
   - Accuracy, detection metrics, classification report
   - Precision, recall, F1-score
   - Optional visualization of anomalies vs. normal traffic

3. **Generate Synthetic Network Packets**  
   Run `generate_synthetic_traffic.py` to create `data/synthetic_traffic.pcap` with simulated TCP/IP packets. This can be inspected using **Wireshark** or **Zeek**.

---

## Project Overview

**`ai_threat_detection.py`**
- Loads and preprocesses synthetic network traffic data
- Trains an Isolation Forest model to detect anomalies
- Evaluates predictions and produces a report

**`generate_synthetic_network_data.py`**
- Generates realistic features (packet size, source/destination ports, protocol, timestamps)
- Mixes normal and abnormal behaviors (port scans, brute-force bursts)
- Exports dataset as CSV

**`generate_synthetic_traffic.py`**
- Uses **Scapy** to create and store packet captures
- Simulates random IPs, port scans, SYN floods

---

## Use Case

This project serves as a **proof-of-concept for AI-based intrusion detection**, bridging:
- Machine learning in cybersecurity
- Threat hunting and network telemetry
- Data analysis for anomaly detection

It is a foundation for advanced research in:
- Threat Intelligence (TI)
- Cloud Security Analytics
- SIEM / SOC Automation

---

## References

- [Microsoft Threat Intelligence Center (MSTIC)](https://www.microsoft.com/security/blog/mstic/)  
- [Scikit-Learn Documentation](https://scikit-learn.org/stable/)  
- [Scapy Packet Manipulation](https://scapy.readthedocs.io/)