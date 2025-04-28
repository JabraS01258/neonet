import psutil
import subprocess
import socket
import platform

def show_network_info():
    print("\n=== Network Interfaces ===\n")
    addrs = psutil.net_if_addrs()

    for interface_name, interface_addresses in addrs.items():
        print(f"Interface: {interface_name}")
        for address in interface_addresses:
            if address.family == 2:  # IPv4
                print(f"  IP Address: {address.address}")
            elif address.family == 17:  # MAC
                print(f"  MAC Address: {address.address}")
        print()

def show_arp_table():
    print("\n=== ARP Table (Devices your machine has seen) ===\n")
    try:
        if platform.system().lower() == "windows":
            result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
        else:
            result = subprocess.run(["arp", "-a"], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error fetching ARP table: {e}")

def show_outbound_connections():
    print("\n=== Outbound Connections ===\n")
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
        print(f"Error checking outbound connections: {e}")

def main_menu():
    while True:
        print("\n=== NeonNet Recon ===")
        print("[1] Show My Network Interfaces (IP, MAC)")
        print("[2] Show Devices Seen (ARP Table)")
        print("[3] Show Outbound Connections")
        print("[4] Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_network_info()
        elif choice == "2":
            show_arp_table()
        elif choice == "3":
            show_outbound_connections()
        elif choice == "4":
            print("Exiting NeonNet Recon. Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main_menu()

