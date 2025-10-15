from scapy.all import IP, TCP, wrpcap
import numpy as np
import os

# Ensure /data directory exists
os.makedirs("data", exist_ok=True)

# Create synthetic network traffic
packets = []

# Generate 1000 synthetic packets
for _ in range(1000):
    # Create an IP packet with random source and destination IP addresses
    packet = IP(src=f"192.168.0.{np.random.randint(1, 255)}",
                dst=f"192.168.1.{np.random.randint(1, 255)}") / \
             TCP(dport=np.random.randint(1, 65535))
    # Append the generated packet to the list
    packets.append(packet)

# Save the packets to a PCAP file
pcap_path = os.path.join("data", "synthetic_traffic.pcap")
wrpcap(pcap_path, packets)

print("Synthetic traffic generated and saved to 'synthetic_traffic.pcap'.")