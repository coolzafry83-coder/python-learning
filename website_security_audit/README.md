# Website Security Audit Tool

A Python-based defensive cybersecurity tool that performs a basic security audit of a website and generates both JSON and HTML security reports.

## Features

* Checks HTTP response status
* Automatically adds HTTPS when needed
* Checks important HTTP security headers
* Calculates a security header score
* Identifies missing security headers
* Assigns severity levels to findings
* Provides security recommendations
* Checks TLS/SSL certificate information
* Shows certificate issuer
* Shows certificate expiry date
* Calculates remaining certificate days
* Detects certificate status
* Generates an overall security risk assessment
* Generates a JSON security report
* Generates a professional HTML security report
* Handles invalid or unreachable websites without crashing

## Security Headers Checked

The tool checks the following HTTP security headers:

* Content-Security-Policy
* X-Frame-Options
* Strict-Transport-Security
* X-Content-Type-Options

## Severity Levels

Missing security headers are assigned different severity levels:

* HIGH
* MEDIUM

The tool also calculates an overall risk level based on the security header score and TLS certificate status.

## TLS Certificate Checks

The tool checks:

* Certificate issuer
* Certificate validity date
* Certificate expiry date
* Remaining days
* Certificate status

Certificate status can be:

* VALID
* EXPIRING SOON
* EXPIRED

## Output Reports

The tool automatically generates two reports after a successful scan.

### JSON Report

```text
security_report.json
```

The JSON report contains structured security assessment data that can be used for further processing, automation, or integration with other tools.

### HTML Report

```text
security_report.html
```

The HTML report provides a readable security assessment containing:

* Website information
* HTTP status
* Security header score
* Security findings
* Severity levels
* Recommendations
* TLS certificate information
* Overall risk assessment

## Requirements

Python 3.x

Install the required library:

```bash
pip install requests
```

The following modules are included with Python:

* ssl
* socket
* datetime
* json

## How to Run

Open PowerShell or terminal in the project directory:

```bash
python website_security_audit.py
```

Enter a website domain when prompted:

```text
Enter website URL: github.com
```

The tool will scan the website and generate the security reports.

## Example

Example result for a website with strong security headers:

```text
Status Code: 200

Security Headers:
[+] Content-Security-Policy: PRESENT
[+] X-Frame-Options: PRESENT
[+] Strict-Transport-Security: PRESENT
[+] X-Content-Type-Options: PRESENT

Header Security Score: 4 / 4

TLS Certificate:
Certificate Status: VALID

Overall Security Assessment:
Risk Level: LOW
Overall Assessment: GOOD
```

Example result for a website with missing security headers:

```text
Header Security Score: 1 / 4

Security Findings:

Finding: Content-Security-Policy
Severity: HIGH
Recommendation: Add this security header

Finding: Strict-Transport-Security
Severity: HIGH
Recommendation: Add this security header

Finding: X-Content-Type-Options
Severity: MEDIUM
Recommendation: Add this security header

Overall Security Assessment:
Risk Level: HIGH
Overall Assessment: HIGH RISK
```

## Error Handling

The tool handles connection failures and invalid domains without displaying a Python traceback.

Example:

```text
Connection Error
Unable to scan this website.
```

## Project Structure

```text
website_security_audit/
│
├── website_security_audit.py
└── README.md
```

Generated report files are created locally after running the scanner:

```text
security_report.json
security_report.html
```

## Project Purpose

This project was created as part of a hands-on cybersecurity learning path focused on defensive security, Python automation, website security assessment, and practical freelance-ready security tools.

## Disclaimer

This tool is intended for authorized defensive security testing and educational purposes only.

Only scan websites that you own or have explicit permission to assess.
