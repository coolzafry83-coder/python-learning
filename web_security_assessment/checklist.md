# Web Security Assessment Checklist

## 1. HTTPS / TLS

* [ ] HTTPS enabled
* [ ] HTTP redirects to HTTPS
* [ ] SSL/TLS certificate valid
* [ ] Weak TLS configuration checked
* [ ] Certificate expiration checked

## 2. Security Headers

* [ ] Content-Security-Policy (CSP)
* [ ] Strict-Transport-Security (HSTS)
* [ ] X-Frame-Options
* [ ] X-Content-Type-Options
* [ ] Referrer-Policy
* [ ] Permissions-Policy

## 3. Cookies

* [ ] Secure flag
* [ ] HttpOnly flag
* [ ] SameSite attribute
* [ ] Sensitive cookies reviewed

## 4. Authentication

* [ ] Login functionality reviewed
* [ ] Password policy reviewed
* [ ] Session management reviewed
* [ ] Logout functionality reviewed
* [ ] Account lockout/rate limiting reviewed

## 5. Authorization / Access Control

* [ ] Access controls reviewed
* [ ] Unauthorized page access tested
* [ ] Horizontal access control considered
* [ ] Vertical access control considered

## 6. Input Validation

* [ ] User input validation reviewed
* [ ] SQL Injection indicators checked
* [ ] Cross-Site Scripting (XSS) indicators checked
* [ ] Command injection indicators considered
* [ ] File upload validation reviewed where applicable

## 7. Information Disclosure

* [ ] Server information exposure checked
* [ ] Debug/error messages checked
* [ ] Sensitive files/directories checked
* [ ] Source code exposure checked
* [ ] Directory listing checked

## 8. HTTP / Application Security

* [ ] HTTP methods reviewed
* [ ] Security-sensitive endpoints identified
* [ ] CORS configuration reviewed
* [ ] Clickjacking protection reviewed
* [ ] Open redirect indicators checked

## 9. Vulnerability Assessment

* [ ] Common web vulnerabilities reviewed
* [ ] Findings validated manually
* [ ] False positives eliminated
* [ ] Risk severity assigned
* [ ] Evidence collected

## 10. Reporting

* [ ] Executive summary prepared
* [ ] Scope documented
* [ ] Methodology documented
* [ ] Findings documented
* [ ] Evidence attached
* [ ] Risk ratings assigned
* [ ] Remediation recommendations provided
* [ ] Final report reviewed

---

## Assessment Rules

* Test only systems where authorization has been obtained.
* Avoid destructive testing.
* Do not access or expose real sensitive data.
* Record evidence for confirmed findings.
* Validate automated findings manually where possible.
