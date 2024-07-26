import socket
import requests

def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip

def get_public_ip():
    response = requests.get("https://api.ipify.org?format=json")
    public_ip = response.json()["ip"]
    return public_ip

def get_ip_details(ip):
    response = requests.get(f"http://ip-api.com/json/{ip}")
    return response.json()

local_ip = get_local_ip()
print(f"Local IP Address: {local_ip}")

public_ip = get_public_ip()
print(f"Public IP Address: {public_ip}")

ip_details = get_ip_details(public_ip)
print("IP Address Details:")
for key, value in ip_details.items():
    print(f"{key}: {value}")
