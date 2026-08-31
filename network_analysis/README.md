# Network Analysis & Traffic Investigation

## Overview

This project documents practical Windows networking and Wireshark network analysis exercises completed in a controlled learning environment.

The objective was to understand how a host communicates on a network, how routing and DNS work, how active and listening connections can be identified, and how network traffic can be inspected using Wireshark.

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

## 3. Skills Demonstrated

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
* Basic network security investigation

---

## 4. Tools Used

* Windows PowerShell
* Windows Command Prompt
* Wireshark
* Google Chrome
* Git / GitHub

---

## 5. Project Structure

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
└── wireshark/
    ├── README.md
    ├── wireshark_01_raw_capture.png
    ├── wireshark_02_dns_filter.png
    ├── wireshark_03_tls_filter.png
    ├── wireshark_04_packet_details.png
    ├── wireshark_05_tcp_syn.png
    ├── wireshark_06_tcp_handshake.png
    └── wireshark_07_dns_query.png
```

---

## 6. Learning Outcome

This practical project provided hands-on experience with host-level network inspection and packet analysis.

The exercises connect basic networking concepts with practical cybersecurity investigation techniques and provide a foundation for the next stage of the cybersecurity roadmap: deeper network analysis and Nmap practical work.
