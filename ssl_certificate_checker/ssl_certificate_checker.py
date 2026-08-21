import ssl
import socket
from datetime import datetime, timezone

hostname = input("Enter website domain: ").strip()

port = 443

context = ssl.create_default_context()

try:
    with socket.create_connection((hostname, port), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as secure_socket:
            certificate = secure_socket.getpeercert()

except (socket.gaierror, socket.timeout, ConnectionRefusedError, ssl.SSLError):
    print("Error: Unable to establish a secure connection.")
    exit()

print("\n" + "=" * 45)
print("SSL/TLS CERTIFICATE CHECKER")
print("=" * 45)

subject = certificate["subject"]
issuer = certificate["issuer"]

valid_from = certificate["notBefore"]
valid_until = certificate["notAfter"]

print("Domain:", subject[0][0][1])
print("Issuer:", issuer[1][0][1])
print("Valid From:", valid_from)
print("Valid Until:", valid_until)

expiry_date = datetime.strptime(
    valid_until, "%b %d %H:%M:%S %Y GMT"
).replace(tzinfo=timezone.utc)

today = datetime.now(timezone.utc)

days_remaining = (expiry_date - today).days

if days_remaining < 0:
    status = "EXPIRED"
elif days_remaining <= 30:
    status = "EXPIRING SOON"
else:
    status = "VALID"

print("Certificate Status:", status)
print("Days Remaining:", days_remaining)
print("=" * 45)