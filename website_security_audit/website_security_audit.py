import json
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

except requests.exceptions.RequestException:
    print("\nConnection Error")
    print("Unable to scan this website.")
    exit()

security_headers = {
    "Content-Security-Policy": "HIGH",
    "X-Frame-Options": "MEDIUM",
    "Strict-Transport-Security": "HIGH",
    "X-Content-Type-Options": "MEDIUM"
}

score = 0
findings = []

print("\nSecurity Headers:")

for header, severity in security_headers.items():

    if response.headers.get(header):
        print("[+] " + header + ": PRESENT")
        score += 1
    else:
        print("[-] " + header + ": MISSING")

        findings.append({
            "header": header,
            "severity": severity
        })

print("\nHeader Security Score:", score, "/", len(security_headers))

print("\n" + "=" * 45)
print("SECURITY FINDINGS")
print("=" * 45)

if findings:
    for finding in findings:
        print("\nFinding:", finding["header"])
        print("Severity:", finding["severity"])
        print("Recommendation: Add this security header")
else:
    print("No security header findings.")

print("=" * 45)

hostname = url.replace("https://", "").replace("http://", "").split("/")[0]

try:
    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443), timeout=10) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as secure_socket:

            certificate = secure_socket.getpeercert()

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

    print("\n" + "=" * 45)
    print("TLS CERTIFICATE")
    print("=" * 45)
    print("Issuer:", issuer_name)
    print("Valid Until:", valid_until)
    print("Days Remaining:", days_remaining)
    print("Certificate Status:", certificate_status)
    print("=" * 45)

except Exception:
    print("\nTLS Certificate: UNABLE TO CHECK")

if score == 4 and certificate_status == "VALID":
    risk_level = "LOW"
    overall_assessment = "GOOD"

elif score >= 2 and certificate_status != "EXPIRED":
    risk_level = "MEDIUM"
    overall_assessment = "NEEDS ATTENTION"

else:
    risk_level = "HIGH"
    overall_assessment = "HIGH RISK"

print("\n" + "=" * 45)
print("OVERALL SECURITY ASSESSMENT")
print("=" * 45)

print("Security Header Score:", score, "/", len(security_headers))
print("TLS Certificate:", certificate_status)
print("Risk Level:", risk_level)
print("Overall Assessment:", overall_assessment)

print("=" * 45)

report = {
    "website": url,
    "http_status": response.status_code,
    "security_header_score": f"{score}/{len(security_headers)}",
    "findings": findings,
    "tls_certificate": {
        "issuer": issuer_name,
        "valid_until": valid_until,
        "days_remaining": days_remaining,
        "status": certificate_status
    },
    "risk_level": risk_level,
    "overall_assessment": overall_assessment
}

with open("security_report.json", "w") as file:
    json.dump(report, file, indent=4)

print("\nReport saved as: security_report.json")

html = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">

    <title>Website Security Audit Report</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
            line-height: 1.6;
        }}

        h1 {{
            border-bottom: 2px solid #333;
            padding-bottom: 10px;
        }}

        h2 {{
            margin-top: 30px;
        }}

        .summary {{
            border: 1px solid #ccc;
            padding: 20px;
            margin-top: 20px;
        }}

        .finding {{
            border: 1px solid #ddd;
            padding: 15px;
            margin: 10px 0;
        }}

        .high {{
            border-left: 6px solid #c0392b;
        }}

        .medium {{
            border-left: 6px solid #f39c12;
        }}

        .low {{
            border-left: 6px solid #27ae60;
        }}

        .status {{
            font-weight: bold;
        }}
    </style>
</head>

<body>

<h1>Website Security Audit Report</h1>

<div class="summary">

<h2>Website Information</h2>

<p><strong>Website:</strong> {url}</p>
<p><strong>HTTP Status:</strong> {response.status_code}</p>

</div>

<h2>Security Header Score</h2>

<p><strong>{score} / {len(security_headers)}</strong></p>

<h2>Security Findings</h2>
"""

if findings:
    for finding in findings:

        severity_class = finding["severity"].lower()

        html += f"""
<div class="finding {severity_class}">

<p>
<strong>Finding:</strong> {finding["header"]}
</p>

<p>
<strong>Severity:</strong> {finding["severity"]}
</p>

<p>
<strong>Recommendation:</strong>
Add this security header.
</p>

</div>
"""
else:
    html += "<p>No security header findings.</p>"

html += f"""

<h2>TLS Certificate</h2>

<div class="summary">

<p><strong>Issuer:</strong> {issuer_name}</p>

<p><strong>Valid Until:</strong> {valid_until}</p>

<p><strong>Days Remaining:</strong> {days_remaining}</p>

<p>
<strong>Status:</strong>
<span class="status">{certificate_status}</span>
</p>

</div>

<h2>Overall Security Assessment</h2>

<div class="summary">

<p><strong>Risk Level:</strong> {risk_level}</p>

<p>
<strong>Overall Assessment:</strong>
{overall_assessment}
</p>

</div>

</body>
</html>
"""
with open("security_report.html", "w", encoding="utf-8") as file:
    file.write(html)

print("HTML report saved as: security_report.html")