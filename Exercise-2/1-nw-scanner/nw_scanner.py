import socket
import ipaddress
import json
import time
import argparse

def save_results(results):
    with open("last_scan_results.json", "w") as file:
        json.dump(results, file)

def load_results():
    try:
        with open("last_scan_results.json", "r") as file:
            return json.load(file)
    except Exception as e:
        return None

def scan_network(target, last_scan_results=None):
    open_ports = []
    ip_network = ipaddress.ip_network(target)
    
    for ip in ip_network.hosts():
        ip_str = str(ip)
        print(ip_str)
        
        for port in range(1, 65535):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(0.1)  
            
            result = sock.connect_ex((ip_str, port))
            if result == 0:
                open_ports.append({"ip": ip_str, "port": port, "protocol": protocol.upper()})
            sock.close()
    
    if last_scan_results:
        new_ports = [port for port in open_ports if port not in last_scan_results]
        if new_ports:
            for port in new_ports:
                print(f"* {port['port']}/{port['protocol']} open")

    save_results(open_ports)

parser = argparse.ArgumentParser(description="Network Scanner")
parser.add_argument("target", help="IP address or CIDR range to scan")
args = parser.parse_args()

last_scan_results = load_results()

while True:
    scan_network(args.target, last_scan_results)
    time.sleep(3600)
