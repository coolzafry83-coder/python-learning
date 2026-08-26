# Linux Authentication Monitor

A practical Python-based Linux security monitoring tool that analyzes system journal logs to detect authentication-related activity and identify potential login security issues.

## Features

The tool performs the following security monitoring tasks:

1. **Linux Journal Analysis**

   * Reads system journal entries using `journalctl`.

2. **Authentication Failure Detection**

   * Searches journal logs for authentication-related failure events.
   * Detects events such as failed passwords, authentication failures, and invalid users.

3. **Failed Authentication Event Count**

   * Counts the number of detected authentication failures.

4. **Security Alert**

   * Generates a warning when authentication failures are detected.
   * Generates a higher-level alert when multiple failures are detected.

5. **Recent Authentication Events**

   * Displays the most recent authentication-related events for investigation.

## Technologies Used

* Python 3
* Linux
* Wazuh
* `subprocess`
* `journalctl`

## Project Structure

```text
linux_auth_monitor/
│
├── linux_auth_monitor.py
└── README.md
```

## How to Run

On a Linux system with `journalctl` available:

```bash
python3 linux_auth_monitor.py
```

## Example Output

```text
=============================================
      LINUX AUTHENTICATION MONITOR
=============================================

Journal entries loaded: 116

Authentication failures detected: 1

Failed Authentication Events:
...

Security Alert:
WARNING: Authentication failure detected.

Recent Authentication Events:
...
```

## Security Concepts Practiced

* Linux authentication monitoring
* System journal analysis
* Authentication failure detection
* Security event detection
* Alert generation
* Log analysis
* Linux command-line tools
* Python system automation
* Basic security monitoring

## Testing Environment

The tool was developed using Python and tested against a Linux environment running in a Wazuh virtual machine.

The project uses real Linux journal data rather than relying only on simulated log files.

## Disclaimer

This project is intended for educational purposes and authorized security monitoring only. Do not analyze systems or logs without proper authorization.

## Future Improvements

Possible future improvements include:

* Better username extraction
* Source IP detection when available in log events
* Configurable alert thresholds
* Failed-login tracking by time window
* JSON/CSV security reports
* Integration with Wazuh alerts
* Automated security dashboards
