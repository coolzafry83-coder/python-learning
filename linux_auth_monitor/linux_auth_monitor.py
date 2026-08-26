import subprocess

print("=" * 45)
print("      LINUX AUTHENTICATION MONITOR")
print("=" * 45)

result = subprocess.run(
    ["journalctl", "--no-pager"],
    capture_output=True,
    text=True
)

print("\nJournal entries loaded:", len(result.stdout.splitlines()))

failed_events = []

for line in result.stdout.splitlines():
    if any(keyword in line.lower() for keyword in [
        "failed password",
        "authentication failure",
        "invalid user"
    ]):
        failed_events.append(line)

print("\nAuthentication failures detected:", len(failed_events))

print("\nFailed Authentication Events:")

for event in failed_events:
    print(event)

print("\nSecurity Alert:")

print("\nRecent Authentication Events:")

auth_events = []

for line in result.stdout.splitlines():
    if any(keyword in line.lower() for keyword in [
        "authentication failure",
        "failed password",
        "accepted password",
        "invalid user"
    ]):
        auth_events.append(line)

for event in auth_events[-5:]:
    print(event)

if len(failed_events) >= 3:
    print("ALERT: Multiple authentication failures detected!")
elif len(failed_events) >= 1:
    print("WARNING: Authentication failure detected.")
else:
    print("No authentication failures detected.")



