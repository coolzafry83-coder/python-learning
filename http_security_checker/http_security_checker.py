import requests
from urllib.parse import urlparse

url = input("Enter website URL: ").strip()

if not url.startswith(("http://", "https://")):
    url = "https://" + url

try:
    parsed = urlparse(url)

    if not parsed.netloc:
        print("Error: Invalid website URL.")
        exit()

    response = requests.get(
        url,
        timeout=10,
        allow_redirects=True,
        headers={"User-Agent": "Mozilla/5.0"}
    )

except requests.exceptions.RequestException as error:
    print("Error: Unable to connect to the website.")
    print("Details:", error)
    exit()

print("\n" + "=" * 55)
print("        WEBSITE SECURITY ASSESSMENT")
print("=" * 55)

print("Target URL:", url)
print("Final URL:", response.url)
print("Status Code:", response.status_code)

security_headers = {
    "Content-Security-Policy": "Helps prevent XSS and code injection attacks",
    "X-Frame-Options": "Helps prevent clickjacking attacks",
    "Strict-Transport-Security": "Enforces HTTPS connections",
    "X-Content-Type-Options": "Helps prevent MIME-type sniffing",
}

score = 0

print("\nSecurity Headers:")
print("-" * 55)

for header, description in security_headers.items():
    value = response.headers.get(header)

    if value:
        print(f"[+] {header}: PRESENT")
        print(f"    Value: {value}")
        score += 1
    else:
        print(f"[-] {header}: MISSING")
        print(f"    Risk: {description}")

total = len(security_headers)
percentage = (score / total) * 100

print("\n" + "-" * 55)
print(f"Security Header Score: {score}/{total} ({percentage:.0f}%)")

if percentage == 100:
    rating = "GOOD"
elif percentage >= 50:
    rating = "NEEDS IMPROVEMENT"
else:
    rating = "WEAK"

print("Overall Rating:", rating)
print("=" * 55)