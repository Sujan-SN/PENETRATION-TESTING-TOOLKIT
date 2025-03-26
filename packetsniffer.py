import scapy.all as scapy

def packet_sniffer(interface):
    scapy.sniff(iface=interface, count=100)
    print("Packet sniffing complete")

# Example usage
interface = "eth0"
packet_sniffer(interface)
