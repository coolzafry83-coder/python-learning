import os
import subprocess

print("=" * 45)
print("        LINUX SECURITY AUDIT TOOL")
print("=" * 45)

# 1. Current User
print("\n[1] CURRENT USER")
print("User:", os.getlogin())

# 2. Running Services
print("\n[2] RUNNING SERVICES")

result = subprocess.run(
    ["systemctl", "--type=service", "--state=running"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print("Running services detected.")
else:
    print("Could not check services.")

# 3. Listening Ports
print("\n[3] LISTENING PORTS")

result = subprocess.run(
    ["ss", "-tuln"],
    capture_output=True,
    text=True
)

if result.returncode == 0:
    print(result.stdout)
else:
    print("Could not check ports.")

# 4. World-Writable Files
print("\n[4] WORLD-WRITABLE FILES")

result = subprocess.run(
    ["find", "/etc", "-type", "f", "-perm", "-o+w"],
    capture_output=True,
    text=True
)

if result.stdout.strip():
    print(result.stdout)
else:
    print("No world-writable files found in /etc.")

# 5. Security Risk Summary
print("\n[5] SECURITY RISK SUMMARY")

risk_score = 0

if result.stdout.strip():
    risk_score += 1

if risk_score == 0:
    print("Risk Level: LOW")
    print("No world-writable files detected in /etc.")
else:
    print("Risk Level: MEDIUM")
    print("World-writable files detected. Review them.")

print("\n" + "=" * 45)
print("AUDIT COMPLETE")
print("=" * 45)
