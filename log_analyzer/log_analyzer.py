with open("security.log", "r") as file:
    logs = file.readlines()

total_logs = len(logs)
failed_logins = 0
successful_logins = 0
ip_addresses = {}

for log in logs:

    if "FAILED" in log:
        failed_logins += 1

        ip = log.split()[-1]

        if ip in ip_addresses:
            ip_addresses[ip] += 1
        else:
            ip_addresses[ip] = 1

    elif "INFO" in log:
        successful_logins += 1


print("===== Security Log Analyzer =====")
print("Total logs:", total_logs)
print("Successful logins:", successful_logins)
print("Failed login attempts:", failed_logins)

print("\nFailed login attempts by IP:")

for ip, count in ip_addresses.items():
    print(ip, "->", count)

print("\nSuspicious IP addresses:")

for ip, count in ip_addresses.items():
    if count >= 3:
        print(ip, "->", count, "failed attempts")