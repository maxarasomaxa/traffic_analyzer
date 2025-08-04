from scapy.all import sniff, IP, TCP
from utils import plot_traffic

packets = []

def analyze_packet(packet):
	if IP in packet:
		pkt_data = {
			"src_ip": packet[IP].src,
			"dst_ip": packet[IP].dst,
			"protocol": "TCP" if TCP in packet else "Other"
		}
		packets.append(pkt_data)
		print(f"Packet: {pkt_data['src_ip']} -> {pkt_data['dst_ip']}")

try:
	sniff(prn=analyze_packet, timeout=30)
finally:
	plot_traffic(packets)
