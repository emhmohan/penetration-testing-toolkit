# penetration_toolkit.py

import requests
from bs4 import BeautifulSoup
import socket

def scan_ports(host, ports=[21, 22, 80, 443, 3306]):
    print(f"[+] Scanning ports on {host}")
    for port in ports:
        try:
            with socket.socket() as s:
                s.settimeout(1)
                result = s.connect_ex((host, port))
                if result == 0:
                    print(f" - Port {port} is OPEN")
        except Exception as e:
            print(f"[!] Error scanning port {port}: {e}")

def basic_directory_bruteforce(url, wordlist=["admin", "login", "dashboard"]):
    print(f"[+] Starting directory brute-force on {url}")
    for word in wordlist:
        full_url = f"{url.rstrip('/')}/{word}"
        try:
            response = requests.get(full_url)
            if response.status_code == 200:
                print(f" - Found: {full_url}")
        except Exception as e:
            print(f"[!] Error accessing {full_url}: {e}")

def extract_forms(url):
    print(f"[+] Extracting forms from {url}")
    try:
        res = requests.get(url)
        soup = BeautifulSoup(res.text, "html.parser")
        forms = soup.find_all("form")
        for i, form in enumerate(forms, 1):
            print(f"Form #{i}: {form}")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    print("=== PENETRATION TESTING TOOLKIT ===")
    print("1. Port Scanner")
    print("2. Directory Bruteforce")
    print("3. Form Extractor
")

    choice = input("Select option (1-3): ")

    if choice == '1':
        target = input("Enter host (e.g., example.com): ")
        scan_ports(target)
    elif choice == '2':
        url = input("Enter target URL (e.g., http://example.com): ")
        basic_directory_bruteforce(url)
    elif choice == '3':
        url = input("Enter target URL (e.g., http://example.com): ")
        extract_forms(url)
    else:
        print("[!] Invalid choice")