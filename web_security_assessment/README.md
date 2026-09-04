# Professional Web Security Assessment

A practical web security assessment project designed to identify common security weaknesses in an authorized web application.

## Objective

The objective of this project is to perform a structured security assessment covering:

* HTTPS / TLS configuration
* Security headers
* Cookies and session security
* Authentication
* Authorization / access control
* Input validation
* Common web vulnerabilities
* Information disclosure
* HTTP/application security
* Risk assessment and remediation

## Tools

* Python
* Requests
* Burp Suite
* Browser Developer Tools
* PowerShell
* Git / GitHub

## Assessment Methodology

The assessment follows a structured workflow:

1. Define authorized scope
2. Perform basic reconnaissance
3. Review HTTP/HTTPS configuration
4. Analyze security headers
5. Review cookies and session controls
6. Review authentication and authorization
7. Check input validation
8. Assess common web security weaknesses
9. Collect evidence
10. Validate findings
11. Assign risk severity
12. Prepare professional security report

## Current Test Target

For development and practice, testing is performed against my own locally hosted cybersecurity portfolio website.

**Target:** `http://localhost:8000`

Testing is performed only on systems where authorization has been obtained.

## Project Files

```text
web_security_assessment/
│
├── assessment.py
├── checklist.md
├── README.md
└── report_template.md
```

## Current Assessment

The initial security-header assessment identified the following missing headers:

| Security Header           | Status  |
| ------------------------- | ------- |
| Content-Security-Policy   | Missing |
| Strict-Transport-Security | Missing |
| X-Frame-Options           | Missing |
| X-Content-Type-Options    | Missing |
| Referrer-Policy           | Missing |

These findings will be validated, documented, assigned risk levels, and included in the final assessment report.

## Disclaimer

This project is intended for authorized security testing, learning, portfolio development, and legitimate security assessment work.

Never test systems without explicit authorization.
