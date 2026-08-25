# Linux Security Audit Tool

A practical Python-based Linux security auditing tool designed to perform basic security checks on a Linux system.

## Features

The tool performs five basic security checks:

1. **Current User**

   * Displays the currently logged-in Linux user.

2. **Running Services**

   * Checks services currently running through `systemctl`.

3. **Listening Ports**

   * Displays TCP/UDP listening ports using `ss`.

4. **World-Writable Files**

   * Searches `/etc` for files that can be modified by other users.

5. **Security Risk Summary**

   * Provides a basic risk level based on detected world-writable files.

## Technologies Used

* Python 3
* Linux
* `subprocess`
* `os`
* `systemctl`
* `ss`
* `find`

## Project Structure

```text
linux_security_audit/
│
├── linux_security_audit.py
└── README.md
```

## How to Run

Clone or copy the project to a Linux system.

Run:

```bash
python3 linux_security_audit.py
```

## Example Output

```text
=============================================
        LINUX SECURITY AUDIT TOOL
=============================================

[1] CURRENT USER
User: wazuh-user

[2] RUNNING SERVICES
Running services detected.

[3] LISTENING PORTS
...

[4] WORLD-WRITABLE FILES
No world-writable files found in /etc.

[5] SECURITY RISK SUMMARY
Risk Level: LOW
No world-writable files detected in /etc.

=============================================
AUDIT COMPLETE
=============================================
```

## Security Concepts Practiced

* Linux user identification
* Service enumeration
* Network port enumeration
* Linux file permissions
* World-writable files
* Basic security risk assessment
* Python system automation

## Disclaimer

This tool is intended for educational purposes and authorized security auditing only. Run it only on systems you own or have permission to test.

## Future Improvements

Possible future improvements include:

* More security checks
* Improved risk scoring
* Security report generation
* Log file output
* Configuration auditing
* Automated vulnerability checks
