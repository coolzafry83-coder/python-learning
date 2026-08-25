print("=" * 45)
print("       LOG SECURITY DETECTOR")
print("=" * 45)

with open("security.log", "r") as file:
    logs = file.readlines()

print("\nTotal log entries:", len(logs))

failed_logins = []

for log in logs:
    if "FAILED" in log:
        failed_logins.append(log)

print("\nFailed login attempts:", len(failed_logins))

from collections import Counter

failed_ips = []

for log in failed_logins:
    ip = log.split()[-1]
    failed_ips.append(ip)

ip_counts = Counter(failed_ips)

print("\nFailed login IPs:")

for ip, count in ip_counts.items():
    print(ip, "->", count, "attempts")

print("\nSecurity Alerts:")

for ip, count in ip_counts.items():
    if count >= 3:
        print("ALERT:", ip, "has", count, "failed login attempts")

successful_logins = []

for log in logs:
    if "SUCCESS" in log:
        successful_logins.append(log)

print("\nSuccessful login attempts:", len(successful_logins))

total_failed = len(failed_logins)

print("\nRisk Assessment:")

if total_failed >= 5:
    print("Risk Level: HIGH")
elif total_failed >= 3:
    print("Risk Level: MEDIUM")
else:
    print("Risk Level: LOW")