# NeonNet Recon

NeonNet Recon is a lightweight command-line tool for inspecting basic
network details on your machine. The `neonnet.py` script displays
interface information, the local ARP table and current outbound
connections.

## Features

- List IP and MAC addresses for all network interfaces (IPv4 and IPv6).
- Display the ARP table so you can see recently discovered devices.
- Show active outbound connections on the host.

## Requirements

- Python 3.12
- The `psutil` package

A self-contained Python environment with `psutil` is provided in the
`neonnet_env` directory. You can use it to run the script without
installing anything globally.

## How to Run

Using your own Python installation:

```bash
pip install psutil
python3 neonnet.py
```

Or run with the bundled environment:

```bash
./neonnet_env/bin/python neonnet.py
```

After starting the tool you'll see a menu:

1. Show network interfaces (IP and MAC information)
2. Show devices seen (ARP table)
3. Show outbound connections
4. Exit

Select an option by entering its number and press Enter.
