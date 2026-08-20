# HTTP Security Header Checker

A Python-based cybersecurity tool that checks a website for important HTTP security headers.

## Features

* Checks HTTP response status code
* Checks Content-Security-Policy
* Checks X-Frame-Options
* Checks Strict-Transport-Security
* Checks X-Content-Type-Options
* Shows PRESENT or MISSING status
* Calculates a security header score
* Handles connection errors
* Automatically adds HTTPS when needed

## Requirements

* Python 3.x
* Python Requests library

Install Requests:

```
pip install requests
```

## Usage

Run the program:

```
python http_security_checker.py
```

Enter a website URL when prompted:

```
Enter website URL: github.com
```

The program will automatically add HTTPS if it is not provided.

## Example Output

```
Enter website URL: github.com

Status Code: 200

Security Headers:
[+] Content-Security-Policy: PRESENT
[+] X-Frame-Options: PRESENT
[+] Strict-Transport-Security: PRESENT
[+] X-Content-Type-Options: PRESENT

Security Score: 4 / 4
```

## Security Headers Checked

### Content-Security-Policy

Controls which resources a browser is allowed to load and helps reduce certain cross-site scripting risks.

### X-Frame-Options

Helps protect websites against clickjacking by controlling whether a page can be loaded inside a frame.

### Strict-Transport-Security

Also known as HSTS. It tells browsers to use HTTPS when communicating with the website.

### X-Content-Type-Options

The `nosniff` value helps prevent browsers from incorrectly guessing the content type of a resource.

## Error Handling

The tool handles connection and request errors and displays a user-friendly error message instead of crashing.

## Learning Objectives

This project demonstrates practical use of:

* Python
* HTTP requests
* HTTP response headers
* Lists and loops
* Conditional statements
* Error handling
* Basic web security concepts
* Security assessment automation

## Disclaimer

This tool is created for educational and authorized security testing purposes. Only test websites that you own or have permission to assess.
