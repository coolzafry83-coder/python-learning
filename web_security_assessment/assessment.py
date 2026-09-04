import requests


def check_security_headers(url):
    try:
        response = requests.get(url, timeout=10)

        headers = response.headers

        security_headers = {
            "Content-Security-Policy": "CSP",
            "Strict-Transport-Security": "HSTS",
            "X-Frame-Options": "X-Frame-Options",
            "X-Content-Type-Options": "X-Content-Type-Options",
            "Referrer-Policy": "Referrer-Policy",
        }

        print("\nSecurity Headers Assessment")
        print("-" * 35)

        for header, name in security_headers.items():
            if header in headers:
                print(f"[PASS] {name}")
            else:
                print(f"[WARN] {name} missing")

    except requests.RequestException as error:
        print(f"Error: {error}")


target = input("Enter authorized website URL: ")

check_security_headers(target)