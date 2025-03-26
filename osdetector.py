import scapy.all as scapy

def os_detector(ip):
    packet = scapy.IP(dst=ip)/scapy.ICMP()
    response = scapy.sr1(packet, timeout=1, verbose=0)
    if response:
        os = response.getlayer(scapy.IP).ttl
        if os <= 64:
            print("Operating System: Linux")
        elif os <= 128:
            print("Operating System: Windows")
        else:
            print("Operating System: Unknown")
    else:
        print("No response received")
