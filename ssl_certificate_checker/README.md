# SSL/TLS Certificate Checker

A Python-based cybersecurity tool that retrieves and analyzes the SSL/TLS certificate of a website.

## Features

- Connects to a website using TLS
- Retrieves the SSL/TLS certificate
- Displays the certificate domain
- Displays the certificate issuer
- Shows certificate validity dates
- Calculates remaining certificate days
- Detects expired certificates
- Detects certificates expiring within 30 days
- Handles connection and SSL errors
- Uses Python's built-in SSL and Socket modules

## Requirements

- Python 3.x

No external Python libraries are required.

## Usage

Run the program:

    python ssl_certificate_checker.py

Enter a website domain:

    Enter website domain: github.com

## Example Output

    =============================================
    SSL/TLS CERTIFICATE CHECKER
    =============================================
    Domain: github.com
    Issuer: Sectigo Limited
    Valid From: Jul  3 00:00:00 2026 GMT
    Valid Until: Sep 30 23:59:59 2026 GMT
    Certificate Status: VALID
    Days Remaining: 40
    =============================================

## Certificate Status

The tool uses the following status rules:

- VALID: More than 30 days remaining
- EXPIRING SOON: 30 days or fewer remaining
- EXPIRED: Certificate expiration date has passed

## Cybersecurity Concepts

This project demonstrates:

- SSL/TLS
- HTTPS
- TLS certificates
- Certificate Authorities
- Certificate expiration
- Socket connections
- Python SSL module
- Error handling
- Security assessment automation

## Learning Purpose

This project was created as part of a practical cybersecurity learning portfolio.

## Disclaimer

This tool is intended for educational purposes and authorized security testing only. Test only websites and systems that you own or have permission to assess.