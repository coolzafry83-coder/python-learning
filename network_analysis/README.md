# Network Analysis & Traffic Investigation

## Overview

This project documents practical Windows networking, Wireshark packet analysis, and Nmap network enumeration exercises completed in a controlled learning environment.

The objective was to understand host networking, routing, DNS, active connections, packet-level traffic, TCP communication, network discovery, port states, service identification, and basic network security observations.

---

## 1. Windows Networking Analysis

The following Windows networking commands were used for practical analysis:

| Task                   | Command                              | Purpose                                                             |
| ---------------------- | ------------------------------------ | ------------------------------------------------------------------- |
| IP Configuration       | `ipconfig /all`                      | Identify IP address, subnet mask, gateway, DNS and network adapters |
| Routing Table          | `route print`                        | Examine local routing information                                   |
| Connectivity Test      | `ping 8.8.8.8`                       | Test network connectivity and latency                               |
| DNS Lookup             | `nslookup google.com`                | Examine DNS name resolution                                         |
| Network Connections    | `netstat -ano`                       | Identify active connections, listening ports and PIDs               |
| Listening Ports        | `Get-NetTCPConnection -State Listen` | Identify TCP services listening on the host                         |
| Process Identification | `Get-Process -Id 3576`               | Identify the process associated with a listening port               |
| System Process         | `Get-Process -Id 4`                  | Identify the Windows System process                                 |
| Network Adapters       | `Get-NetAdapter`                     | Inspect network interfaces and their status                         |
| ARP Table              | `arp -a`                             | Examine IP-to-MAC address mappings                                  |

### Evidence

Screenshots for these tasks are stored in:

`windows_networking/`

---

## 2. Wireshark Network Analysis

Wireshark was used to capture and inspect network traffic.

### Practical Activities

* Captured live network traffic over Wi-Fi
* Applied DNS traffic filtering
* Identified TLS/HTTPS traffic
* Inspected packet protocol layers
* Identified TCP SYN packets
* Observed the TCP three-way handshake
* Inspected DNS query details
* Checked for HTTP traffic

### TCP Three-Way Handshake

The TCP connection establishment process was identified as:

```text
SYN → SYN-ACK → ACK
```

This demonstrates the basic process used to establish a TCP connection.

### HTTPS/TLS Observation

TLS traffic was observed during web browsing. The traffic was encrypted, demonstrating why HTTPS traffic cannot normally be read like plain HTTP traffic from a packet capture.

### DNS Observation

DNS packets were inspected to identify domain-name queries and understand how domain names are resolved to IP addresses.

### HTTP Observation

An HTTP display filter was tested. No HTTP packets were observed in the capture, which is consistent with the website traffic being delivered over HTTPS/TLS.

### Evidence

Wireshark screenshots are stored in:

`wireshark/`

---

## 3. Nmap Network Enumeration

Nmap was used for practical network enumeration against the user's own localhost and VirtualBox Host-Only lab interface.

### Practical Activities

| Task                      | Command                                                    | Purpose                                                      |
| ------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| Basic Scan                | `nmap 127.0.0.1`                                           | Identify common open TCP ports                               |
| Service Version Detection | `nmap -sV 127.0.0.1`                                       | Identify services and versions                               |
| Full TCP Scan             | `nmap -p- 127.0.0.1`                                       | Scan all TCP ports from 1-65535                              |
| Targeted Service Scan     | `nmap -sV -p 135,445,3306,5040,5357,33060 127.0.0.1`       | Perform focused service enumeration                          |
| OS Detection              | `nmap -O 127.0.0.1`                                        | Identify the probable operating system                       |
| Default NSE Scripts       | `nmap -sC -sV -p 135,445,3306,5357,33060 127.0.0.1`        | Collect additional service information using default scripts |
| UDP Scan                  | `nmap -sU -p 53,67,68,123,137,138,161,5353,5355 127.0.0.1` | Examine selected UDP ports                                   |
| Port State Reasoning      | `nmap -p 135,445,3306,5040,5357,33060 --reason 127.0.0.1`  | Understand why Nmap classified ports as open                 |
| Network Discovery         | `nmap -sn 192.168.56.0/24`                                 | Discover active hosts on the local VirtualBox lab network    |
| Lab Service Scan          | `nmap -sV -p 135,139,445,3306,5357 192.168.56.1`           | Identify services on the discovered lab host                 |

### Key Findings

The localhost scan identified several listening services, including:

* Microsoft Windows RPC on port `135`
* Microsoft-DS/SMB on port `445`
* MySQL `8.0.46` on port `3306`
* Microsoft HTTPAPI on port `5357`
* MySQL X Protocol on port `33060`

The full TCP scan identified additional listening ports, demonstrating why a limited default-port scan may not reveal every listening service.

The UDP scan identified several ports as `open|filtered`, demonstrating that UDP port-state determination can differ from TCP because UDP services may not respond directly to probes.

OS detection identified the system as Microsoft Windows.

The VirtualBox Host-Only network `192.168.56.0/24` was also discovered and analyzed in the controlled lab environment.

### Security Observations

The Nmap results demonstrated the importance of:

* Identifying unnecessary exposed services
* Understanding listening ports
* Mapping services to applications
* Reviewing SMB exposure
* Checking database service exposure
* Understanding TCP and UDP port states
* Performing enumeration before deeper security testing

These observations are for the user's own systems and controlled lab environment.

### Evidence

Nmap screenshots are stored in:

`nmap/`

---

## 4. Skills Demonstrated

* Windows networking fundamentals
* IPv4 configuration analysis
* Routing table analysis
* DNS troubleshooting
* Network connectivity testing
* TCP connection analysis
* Port and process identification
* ARP analysis
* Network adapter inspection
* Wireshark packet capture
* DNS traffic analysis
* TCP handshake analysis
* TLS/HTTPS traffic identification
* Nmap host discovery
* TCP and UDP port scanning
* Service/version enumeration
* OS detection
* Basic NSE usage
* Port-state interpretation
* Basic network security investigation

---

## 5. Tools Used

* Windows PowerShell
* Windows Command Prompt
* Wireshark
* Nmap
* Google Chrome
* Git / GitHub
* VirtualBox

---

## 6. Project Structure

```text
network_analysis/
│
├── README.md
│
├── windows_networking/
│   ├── windows_01_ipconfig.png
│   ├── windows_02_route_print_01.png
│   ├── windows_02_route_print_02.png
│   ├── windows_03_ping.png
│   ├── windows_04_nslookup.png
│   ├── windows_05_netstat_01.png
│   ├── windows_05_netstat_02.png
│   ├── windows_05_netstat_03.png
│   ├── windows_06_listening_ports.png
│   ├── windows_07_mysql_process.png
│   ├── windows_08_system_process.png
│   ├── windows_09_netadapter.png
│   └── windows_10_arp.png
│
├── wireshark/
│   ├── README.md
│   ├── wireshark_01_raw_capture.png
│   ├── wireshark_02_dns_filter.png
│   ├── wireshark_03_tls_filter.png
│   ├── wireshark_04_packet_details.png
│   ├── wireshark_05_tcp_syn.png
│   ├── wireshark_06_tcp_handshake.png
│   └── wireshark_07_dns_query.png
│
└── nmap/
    ├── nmap_01_basic_and_version_scan.png
    ├── nmap_02_full_tcp_scan.png
    ├── nmap_03_targeted_service_scan.png
    ├── nmap_04_os_detection.png
    ├── nmap_05_default_scripts.png
    ├── nmap_06_udp_scan.png
    ├── nmap_07_port_state_reason.png
    ├── nmap_08_network_discovery.png
    ├── nmap_09_lab_host_scan.png
    └── nmap_10_lab_service_version.png
```

---

## 7. Learning Outcome

This practical project provided hands-on experience with host-level network inspection, packet analysis, network enumeration, service identification, and basic security investigation.

The project connects fundamental networking concepts with practical cybersecurity techniques and provides a foundation for the next stages of the cybersecurity roadmap:

**Linux Networking → Wireshark → Nmap → Deeper Web Security → Sellable Cybersecurity Services → Client Hunting**

The next planned stage is deeper web security practice followed by preparation of practical, client-facing cybersecurity services.
