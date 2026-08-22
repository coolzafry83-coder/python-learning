import requests
import ssl
import socket
from datetime import datetime, timezone

url = input("Enter website URL: ").strip()

if not url.startswith("http"):
    url = "https://" + url

try:
    response = requests.get(url, timeout=10)
    print("Status Code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("\nConnection Error:", e)
    print("Unable to scan this website.")
    exit()


score = 0

security_headers = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "X-Content-Type-Options"
]

print("\nSecurity Headers:")

for header in security_headers:
    value = response.headers.get(header)

    if value:
        print("[+] " + header + ": PRESENT")
        score += 1
    else:
        print("[-] " + header + ": MISSING")

print("\nHeader Security Score:", score, "/", len(security_headers))


hostname = url.replace("https://", "").replace("http://", "").split("/")[0]

context = ssl.create_default_context()

try:
    with socket.create_connection((hostname, 443), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as secure_socket:
            certificate = secure_socket.getpeercert()

except (socket.gaierror, socket.timeout, ConnectionRefusedError, ssl.SSLError):
    print("\nTLS Certificate: Unable to retrieve")
    certificate = None


if certificate:
    issuer = certificate["issuer"]
    valid_until = certificate["notAfter"]

    issuer_name = issuer[1][0][1]

    expiry_date = datetime.strptime(
        valid_until, "%b %d %H:%M:%S %Y GMT"
    ).replace(tzinfo=timezone.utc)

    today = datetime.now(timezone.utc)

    days_remaining = (expiry_date - today).days

    if days_remaining < 0:
        certificate_status = "EXPIRED"
    elif days_remaining <= 30:
        certificate_status = "EXPIRING SOON"
    else:
        certificate_status = "VALID"

    print("\nTLS Certificate:")
    print("Issuer:", issuer_name)
    print("Valid Until:", valid_until)
    print("Days Remaining:", days_remaining)
    print("Certificate Status:", certificate_status)

    print("\n" + "=" * 45)
print("SECURITY SUMMARY")

print("HTTP Status:", response.status_code)
print("Security Header Score:", score, "/", len(security_headers))

if certificate:
    print("TLS Certificate:", certificate_status)
    print("Certificate Days Remaining:", days_remaining)

if score == len(security_headers) and certificate and certificate_status == "VALID":
    assessment = "GOOD"
else:
    assessment = "NEEDS ATTENTION"

print("Overall Assessment:", assessment)

print("=" * 45)