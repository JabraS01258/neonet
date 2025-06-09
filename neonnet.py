import psutil
import subprocess
import socket
import platform

HEADER = "\033[96m\033[1m"  # Bright cyan
OPTION = "\033[93m\033[1m"  # Bright yellow
GREEN = "\033[92m"
MAGENTA = "\033[95m"
RED = "\033[91m"
RESET = "\033[0m"

def show_network_info():
    print(f"\n{HEADER}=== Network Interfaces ==={RESET}\n")
    addrs = psutil.net_if_addrs()

    for interface_name, interface_addresses in addrs.items():
        print(f"{GREEN}{interface_name}{RESET}")
        for address in interface_addresses:
            if address.family == 2:  # IPv4
                print(f"  IP: {MAGENTA}{address.address}{RESET}")
            elif address.family == 17:  # MAC
                print(f"  MAC: {MAGENTA}{address.address}{RESET}")
        print()

def show_arp_table():
    print(f"\n{HEADER}=== ARP Table (Devices your machine has seen) ==={RESET}\n")
    try:
        if platform.system().lower() == "windows":
            result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
        else:
            result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"{RED}Error fetching ARP table: {e}{RESET}")

def show_outbound_connections():
    print(f"\n{HEADER}=== Outbound Connections ==={RESET}\n")
    try:
        if platform.system().lower() == "windows":
            # Windows: use netstat
            result = subprocess.run(["netstat", "-ano"], capture_output=True, text=True)
        else:
            # Linux/WSL: use ss
            result = subprocess.run(["ss", "-tunap"], capture_output=True, text=True)

        if result.stdout:
            lines = result.stdout.splitlines()
            for line in lines:
                print(line)
        else:
            print("No outbound connections found.")
    except Exception as e:
        print(f"{RED}Error checking outbound connections: {e}{RESET}")

def main_menu():
    while True:
        print(f"\n{HEADER}=== NeonNet Recon ==={RESET}")
        print(f"{OPTION}[1]{RESET} Show My Network Interfaces (IP, MAC)")
        print(f"{OPTION}[2]{RESET} Show Devices Seen (ARP Table)")
        print(f"{OPTION}[3]{RESET} Show Outbound Connections")
        print(f"{OPTION}[4]{RESET} Exit")
        choice = input(f"{HEADER}Choose an option: {RESET}").strip()

        if choice == "1":
            show_network_info()
        elif choice == "2":
            show_arp_table()
        elif choice == "3":
            show_outbound_connections()
        elif choice == "4":
            print(f"{HEADER}Exiting NeonNet Recon. Goodbye!{RESET}")
            break
        else:
            print(f"{RED}Invalid choice. Please select 1, 2, 3, or 4.{RESET}")

if __name__ == "__main__":
    main_menu()

