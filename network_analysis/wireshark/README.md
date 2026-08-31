# Wireshark Network Traffic Analysis

## Overview

This practical exercise used Wireshark to capture and analyze network traffic in a controlled learning environment.

The objective was to understand DNS, TCP, TLS/HTTPS traffic, packet structure, and basic network communication.

## Practical Tasks

### 1. Raw Traffic Capture

Captured live network packets from the active Wi-Fi interface.

### 2. DNS Traffic

Applied the following display filter:

```text
dns
```

Inspected DNS queries and domain-name resolution traffic.

### 3. TLS/HTTPS Traffic

Identified encrypted TLS traffic generated during HTTPS web browsing.

### 4. Packet Details

Inspected protocol layers including:

```text
Frame
Ethernet II
IPv4
TCP
TLS
```

### 5. TCP SYN Packets

Used:

```text
tcp.flags.syn == 1
```

to identify TCP SYN packets.

### 6. TCP Three-Way Handshake

Observed the TCP connection establishment sequence:

```text
SYN → SYN-ACK → ACK
```

### 7. DNS Query Inspection

Expanded the DNS query information to inspect the requested domain.

### 8. HTTP Traffic Check

Tested the following filter:

```text
http
```

No HTTP packets were observed in the capture. The observed web traffic was using encrypted HTTPS/TLS communication.

## Evidence

Screenshots are stored in this directory:

```text
wireshark/
```

## Skills Demonstrated

* Wireshark packet capture
* Display filters
* DNS analysis
* TCP analysis
* TCP three-way handshake
* TLS/HTTPS identification
* Packet-layer inspection
* Basic network traffic investigation

## Tools

* Wireshark
* Windows Wi-Fi networking
* Google Chrome

## Learning Outcome

This exercise developed practical understanding of how network traffic can be captured, filtered, and investigated using Wireshark. It provides a foundation for deeper network analysis and Nmap-based security assessment.
