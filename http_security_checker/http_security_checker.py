import requests

url = input("Enter website URL: ").strip()

if not url.startswith(("http://", "https://")):
    url = "https://" + url

try:
    response = requests.get(url, timeout=10)
except requests.exceptions.RequestException:
    print("Error: Unable to connect to the website.")
    exit()

print("Status Code:", response.status_code)

security_headers = [
    "Content-Security-Policy",
    "X-Frame-Options",
    "Strict-Transport-Security",
    "X-Content-Type-Options"
]

score = 0

print("\nSecurity Headers:")

for header in security_headers:
    value = response.headers.get(header)

    if value:
        print("[+] " + header + ": PRESENT")
        score += 1
    else:
        print("[-] " + header + ": MISSING")

print("\nSecurity Score:", score, "/", len(security_headers))

    