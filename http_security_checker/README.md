# Website Security Assessment Tool

A Python-based security assessment tool that performs a basic, non-destructive check of a website's HTTP security configuration.

The tool analyzes HTTP response headers and provides a simple security score and overall rating.

## Features

* Checks HTTP response status code
* Detects HTTP security headers
* Shows PRESENT or MISSING status
* Displays detected header values
* Explains the security purpose/risk of missing headers
* Calculates a security header score
* Provides an overall security rating
* Follows redirects and shows the final URL
* Validates the target URL
* Handles connection and request errors
* Automatically adds HTTPS when no protocol is provided
* Uses a browser-like User-Agent

## Security Checks

The following HTTP security headers are assessed:

| Header                    | Security Purpose                                |
| ------------------------- | ----------------------------------------------- |
| Content-Security-Policy   | Helps reduce XSS and other code-injection risks |
| X-Frame-Options           | Helps protect against clickjacking              |
| Strict-Transport-Security | Enforces HTTPS connections through HSTS         |
| X-Content-Type-Options    | Helps prevent MIME-type sniffing                |

## Requirements

* Python 3.x
* Requests library

Install Requests:

```bash
pip install requests
```

## Usage

Run the tool:

```bash
python http_security_checker.py
```

Enter a website URL:

```text
Enter website URL: https://example.com
```

If `http://` or `https://` is not provided, the tool automatically uses HTTPS.

## Example Assessment

```text
=======================================================
        WEBSITE SECURITY ASSESSMENT
=======================================================
Target URL: https://example.com
Final URL: https://example.com/
Status Code: 200

Security Headers:
-------------------------------------------------------
[-] Content-Security-Policy: MISSING
    Risk: Helps prevent XSS and code injection attacks
[-] X-Frame-Options: MISSING
    Risk: Helps prevent clickjacking attacks
[-] Strict-Transport-Security: MISSING
    Risk: Enforces HTTPS connections
[-] X-Content-Type-Options: MISSING
    Risk: Helps prevent MIME-type sniffing

-------------------------------------------------------
Security Header Score: 0/4 (0%)
Overall Rating: WEAK
=======================================================
```

## Assessment Method

The tool performs a basic HTTP response-header assessment.

It does **not** attempt exploitation, authentication bypass, destructive testing, or modification of the target website.

A missing security header does not automatically mean that a website is vulnerable. The results should be reviewed in the context of the application's architecture and security requirements.

## Security Rating

The current scoring model evaluates four security headers:

* **4/4 (100%)** - GOOD
* **2-3/4 (50-75%)** - NEEDS IMPROVEMENT
* **0-1/4 (0-25%)** - WEAK

This score is intended as a quick configuration indicator, not a complete penetration-test rating.

## Project Purpose

This project demonstrates practical cybersecurity skills including:

* Python security automation
* HTTP requests and responses
* HTTP security headers
* Web security fundamentals
* Security configuration assessment
* Error handling
* Basic vulnerability identification
* Security reporting concepts

## Portfolio Evidence

Assessment evidence is captured from authorized/test targets and can be used to demonstrate the tool's functionality.

Example evidence:

`example_com_security_assessment.png`

## Ethical Use

This tool is intended for educational purposes and authorized security assessments only.

**Only assess websites and systems that you own or have explicit permission to test.**

The author is not responsible for unauthorized or illegal use of this tool.
