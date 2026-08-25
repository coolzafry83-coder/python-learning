# Log Security Detector

A practical Python-based security log analysis tool that detects suspicious login activity and generates a basic security risk assessment.

## Features

The tool analyzes security log entries and performs the following checks:

1. **Log Entry Count**

   * Counts the total number of log entries.

2. **Failed Login Detection**

   * Identifies failed login attempts.

3. **IP Address Analysis**

   * Extracts IP addresses associated with failed logins.
   * Counts failed attempts per IP address.

4. **Security Alert Detection**

   * Generates an alert when an IP address has three or more failed login attempts.

5. **Successful Login Detection**

   * Counts successful login attempts.

6. **Risk Assessment**

   * Assigns a basic risk level based on the number of failed login attempts:

     * 0–2 = LOW
     * 3–4 = MEDIUM
     * 5+ = HIGH

## Technologies Used

* Python 3
* Linux
* Wazuh
* Python `collections.Counter`

## Project Structure

```text
log_security_detector/
│
├── log_security_detector.py
├── security.log
└── README.md
```

## How to Run

Run the tool using Python 3:

```bash
python3 log_security_detector.py
```

## Example Detection

```text
Total log entries: 5

Failed login attempts: 3

Failed login IPs:
192.168.1.50 -> 3 attempts

Security Alerts:
ALERT: 192.168.1.50 has 3 failed login attempts

Successful login attempts: 2

Risk Assessment:
Risk Level: MEDIUM
```

## Security Concepts Practiced

* Log analysis
* Failed login detection
* IP address analysis
* Authentication monitoring
* Brute-force detection logic
* Security alert generation
* Basic risk assessment
* Python automation
* Linux security monitoring
* Wazuh-based testing

## Testing Environment

The tool was developed using Python and tested in a Linux environment using a Wazuh virtual machine.

## Disclaimer

This project is intended for educational purposes and authorized security monitoring only. Do not use it to analyze systems or logs without proper authorization.

## Future Improvements

Possible future improvements include:

* Real Linux authentication log analysis
* Automatic detection of multiple suspicious IPs
* Configurable detection thresholds
* CSV/JSON security reports
* Timestamp-based attack detection
* Integration with Wazuh alerts
