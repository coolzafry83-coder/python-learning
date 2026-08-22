# Website Security Scanner

A Python-based cybersecurity tool that performs a basic security assessment of a website by checking its HTTP response, security headers, and SSL/TLS certificate.

## Features

- Accepts a website URL or domain name
- Automatically adds HTTPS when needed
- Checks HTTP response status code
- Checks important HTTP security headers
- Calculates a security header score
- Retrieves SSL/TLS certificate information
- Displays certificate issuer
- Displays certificate expiration date
- Calculates remaining certificate days
- Detects valid certificates
- Detects certificates expiring within 30 days
- Detects expired certificates
- Generates an overall security assessment
- Handles connection errors gracefully

## Security Headers Checked

The scanner checks the following HTTP security headers:

- Content-Security-Policy
- X-Frame-Options
- Strict-Transport-Security
- X-Content-Type-Options

## Requirements

Python 3.x

Install the required library:

    pip install requests

The following modules are included with Python:

- ssl
- socket
- datetime

## Usage

Run the program:

    python website_security_scanner.py

Enter a website domain or URL:

    Enter website URL: github.com

The tool will perform a basic security assessment and display the results.

## Example Output

    Enter website URL: github.com

    Status Code: 200

    Security Headers:
    [+] Content-Security-Policy: PRESENT
    [+] X-Frame-Options: PRESENT
    [+] Strict-Transport-Security: PRESENT
    [+] X-Content-Type-Options: PRESENT

    Header Security Score: 4 / 4

    TLS Certificate:
    Issuer: Sectigo Limited
    Valid Until: Sep 30 23:59:59 2026 GMT
    Days Remaining: 39
    Certificate Status: VALID

    =============================================
    SECURITY SUMMARY
    =============================================
    HTTP Status: 200
    Security Header Score: 4 / 4
    TLS Certificate: VALID
    Certificate Days Remaining: 39
    Overall Assessment: GOOD
    =============================================

## Security Assessment

The tool provides a basic assessment based on:

- HTTP response status
- Security header presence
- TLS certificate status
- Certificate expiration

A website receives a "GOOD" assessment when all checked security headers are present and the TLS certificate is valid.

If security headers are missing or the certificate requires attention, the tool reports:

    Overall Assessment: NEEDS ATTENTION

## Error Handling

The scanner handles connection and network errors without displaying a Python traceback to the user.

Example:

    Connection Error: Unable to connect to the website.
    Unable to scan this website.

## Cybersecurity Concepts Demonstrated

This project demonstrates practical understanding of:

- HTTP requests
- HTTP response status codes
- HTTP security headers
- HTTPS
- SSL/TLS
- Digital certificates
- Certificate Authorities
- Certificate expiration
- Socket connections
- Security assessment automation
- Python exception handling

## Project Purpose

This project was developed as part of a practical cybersecurity learning portfolio.

It combines concepts from HTTP security header analysis and SSL/TLS certificate checking into a single basic website security assessment tool.

## Limitations

This is a basic security assessment tool.

It does not perform:

- Vulnerability exploitation
- Penetration testing
- Port scanning
- SQL injection testing
- XSS testing
- Full web application vulnerability scanning

For authorized security assessment and educational purposes only.

## Disclaimer

This tool is intended for educational purposes and authorized security testing only.

Only scan websites and systems that you own or have explicit permission to assess.