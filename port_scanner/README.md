# TCP Port Scanner

A Python-based defensive cybersecurity tool that scans a target IP address across a user-defined TCP port range and identifies open ports and common services.

## Features

* Scans TCP ports
* Accepts a target IP address
* Allows a custom start and end port
* Detects open TCP ports
* Hides closed ports for cleaner output
* Identifies common services
* Displays scan completion status
* Counts total open ports
* Uses connection timeout to prevent hanging
* Designed for authorized defensive security testing

## Services Identified

The scanner identifies these common services:

* Port 22 → SSH
* Port 80 → HTTP
* Port 443 → HTTPS
* Port 8080 → HTTP-ALT

For other open ports, the tool displays:

```text
Service: Unknown
```

## Requirements

Python 3.x

The project uses Python's built-in `socket` module, so no external package installation is required.

## How to Run

Open PowerShell or terminal inside the project directory:

```bash
python port_scanner.py
```

The tool will ask for:

```text
Enter IP address:
Enter start port:
Enter end port:
```

Example:

```text
Enter IP address: 127.0.0.1
Enter start port: 8080
Enter end port: 8080
```

## Example Output

```text
Scanning: 127.0.0.1
==============================

TCP Port 8080: OPEN | Service: HTTP-ALT

Scan Complete
Open Ports: 1
```

## Testing with a Local HTTP Server

For safe local testing, start a Python HTTP server:

```bash
python -m http.server 8080
```

Then run the scanner from another terminal:

```bash
python port_scanner.py
```

Use:

```text
IP address: 127.0.0.1
Start port: 8080
End port: 8080
```

Expected result:

```text
TCP Port 8080: OPEN | Service: HTTP-ALT
```

## How It Works

The tool uses a TCP socket connection to test each port.

Conceptually:

```text
Target IP
    ↓
Port Range
    ↓
TCP Connection Attempt
    ↓
Open or Closed
    ↓
Service Identification
    ↓
Security Scan Result
```

An open port means a service is accepting TCP connections on that port.

A closed port means no service accepted the TCP connection.

## Project Structure

```text
port_scanner/
│
├── port_scanner.py
└── README.md
```

## Cybersecurity Use

Port scanning is a basic network security assessment technique.

It can help identify:

* Exposed services
* Unexpected open ports
* Potential attack surface
* Basic network configuration issues

This project demonstrates practical understanding of:

* TCP
* IP addresses
* Ports
* Sockets
* Client-server communication
* Basic network reconnaissance
* Python automation

## Future Improvements

Possible future improvements include:

* Better service detection
* Scan timing improvements
* Exporting scan results
* Improved reporting
* Basic network audit integration

## Disclaimer

This tool is intended for authorized defensive security testing and educational purposes only.

Only scan systems, networks, and devices that you own or have explicit permission to assess.
