# Security Log Analyzer

A beginner Python project that analyzes security logs and detects failed login attempts.

## Project Purpose

This project reads a security log file and analyzes login activity. It counts successful logins, failed login attempts, and identifies suspicious IP addresses with multiple failed login attempts.

## Features

- Reads security logs from a file
- Counts total log entries
- Counts successful logins
- Counts failed login attempts
- Tracks failed login attempts by IP address
- Detects suspicious IP addresses

## Example Output

===== Security Log Analyzer =====
Total logs: 7
Successful logins: 3
Failed login attempts: 4

Failed login attempts by IP:
192.168.1.10 -> 3
192.168.1.15 -> 1

Suspicious IP addresses:
192.168.1.10 -> 3 failed attempts

## Skills Practiced

- Python file handling
- open()
- readlines()
- for loops
- if/elif statements
- Dictionaries
- String methods
- Counters
- Basic security log analysis

## Files

- `log_analyzer.py` - Main Python program
- `security.log` - Sample security log file
- `README.md` - Project documentation

## How to Run

1. Make sure Python is installed.
2. Open the project folder in VS Code.
3. Run:

python log_analyzer.py

## Project Level

Beginner Python Security Project

Skills Practiced
Python file handling
open()
readlines()
for loops
if/elif
Dictionaries
String methods
Basic security log analysis