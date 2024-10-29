import requests
import socket
from urllib.parse import urlparse
import subprocess
from config import WHOIS_API_KEY  # Import the API key
import os

# ANSI color codes for styling
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    CYAN = '\033[96m'
    RED = '\033[91m'
    ENDC = '\033[0m'   # Reset color

# Clear screen function
def clear_screen():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')

# Display name with styling
def display_name():
    print(f"{Colors.HEADER}WELCOME TO GET WEB INFO BY THEEUNBOTHERED{Colors.ENDC}\n")

# WHOIS Information using WHOIS XML API
def get_whois_info(domain):
    url = f"https://www.whoisxmlapi.com/whoisserver/WhoisService?apiKey={WHOIS_API_KEY}&domainName={domain}&outputFormat=json"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            whois_data = response.json()
            print("\nWHOIS Information:")
            print(whois_data)
        else:
            print(f"WHOIS lookup failed with status code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Error fetching WHOIS information: {e}")

# IP Address Retrieval
def get_ip_address(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"\nIP Address: {ip}")
    except socket.error as e:
        print(f"Error resolving IP: {e}")

# HTTP Headers Retrieval
def get_http_headers(url):
    try:
        response = requests.get(url)
        print("\nHTTP Headers:")
        for header, value in response.headers.items():
            print(f"{header}: {value}")
    except requests.RequestException as e:
        print(f"Error fetching HTTP headers: {e}")

# DNS Records Retrieval using dig command
def get_dns_records(domain):
    try:
        print("\nDNS Records:")
        for record_type in ['A', 'NS', 'MX', 'TXT']:
            result = subprocess.run(['dig', '+short', domain, record_type], capture_output=True, text=True)
            if result.stdout:
                print(f"{record_type} Record:\n{result.stdout.strip()}")
            else:
                print(f"No {record_type} records found.")
    except Exception as e:
        print(f"Error fetching DNS records: {e}")

def main():
    # Clear the screen before displaying the interface
    clear_screen()

    # Display the styled name
    display_name()

    # Ask the user to choose the type of information they want to gather
    print(f"Select the information you want to gather:")
    print(f"{Colors.CYAN}(1. IP Address){Colors.ENDC}")
    print(f"{Colors.GREEN}(2. HTTP Headers){Colors.ENDC}")
    print(f"{Colors.BLUE}(3. WHOIS Information){Colors.ENDC}")
    print(f"{Colors.RED}(4. DNS Records){Colors.ENDC}")
    print(f"{Colors.HEADER}(5. All of the above){Colors.ENDC}")

    choice = input("\nEnter your choice (1-5): ")
    url_input = input("Enter target domain (e.g., example.com or https://example.com): ")
    parsed_url = urlparse(url_input)
    domain = parsed_url.netloc if parsed_url.netloc else parsed_url.path

    print(f"\nGathering information for: {domain}")

    # Run functions based on the user's choice
    if choice == "1":
        get_ip_address(domain)
    elif choice == "2":
        get_http_headers(f"http://{domain}")
    elif choice == "3":
        get_whois_info(domain)
    elif choice == "4":
        get_dns_records(domain)
    elif choice == "5":
        get_ip_address(domain)
        get_http_headers(f"http://{domain}")
        get_whois_info(domain)
        get_dns_records(domain)
    else:
        print("Invalid choice. Please select a number between 1 and 5.")

if __name__ == "__main__":
    main()
