# NeonNet Recon

NeonNet Recon is a lightweight network scanning and reconnaissance tool written in Python 3.12. It provides quick commands for inspecting your local machine's network configuration.

## Features

- Display IP and MAC addresses for all detected network interfaces (IPv4 and IPv6).
- Show the local ARP table to see recently discovered devices.
- List active outbound connections.

## Requirements

- Python 3.12
- The `psutil` package (`pip install psutil`)

If you wish to use the bundled virtual environment, run commands with `./neonnet_env/bin/python` instead of `python3`.

## How to Run

```bash
python3 neonnet.py
```

