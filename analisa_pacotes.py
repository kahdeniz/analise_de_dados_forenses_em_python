from scapy.all import rdpcap, IP, TCP
from collections import Counter
try:
 pacotes = rdpcap("network_traffic.pcap")
 tcp_packets = [pkt for pkt in pacotes if TCP in pkt]
 ip_sources = [pkt[IP].src for pkt in tcp_packets if IP in pkt]
 ip_counts = Counter(ip_sources).most_common(10)
 print("\nTop 10 IPs de origem mais frequentes:")
 for ip, count in ip_counts:
 print(f"{ip}: {count} pacotes")
except FileNotFoundError:
 print("\n[!] Arquivo network_traffic.pcap nao encontrado.")
