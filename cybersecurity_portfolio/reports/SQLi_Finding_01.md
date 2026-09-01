# Security Assessment Finding #1

## SQL Injection in `category` Parameter

**Severity:** High (Lab Assessment)
**Assessment Type:** Authorized Web Security Lab
**Platform:** PortSwigger Web Security Academy
**Affected Endpoint:** `GET /filter`
**Affected Parameter:** `category`

---

## 1. Vulnerability Description

The `category` parameter was found to be vulnerable to SQL injection.

During testing, a normal category value returned only the products belonging to the selected category. A modified input containing a SQL condition changed the application's query behavior and caused additional products to be returned.

This demonstrates that user-controlled input can influence the application's SQL query logic.

---

## 2. Evidence

### Baseline Request

```text
GET /filter?category=Lifestyle
```

**Result:** 3 products returned.

### Modified Request

```text
GET /filter?category=Lifestyle' OR 1=1--
```

**Result:** 8 products returned.

The change from **3 products to 8 products** demonstrates that the application's filtering behavior was altered by the injected SQL condition.

---

## 3. Reproduction Steps

1. Open the authorized PortSwigger SQL Injection lab.
2. Navigate to the product category filter.
3. Select the **Lifestyle** category.
4. Capture the request using Burp Suite.
5. Send the request to **Burp Repeater**.
6. Send the baseline request:

```text
GET /filter?category=Lifestyle
```

7. Observe that 3 products are returned.
8. Modify the parameter to:

```text
GET /filter?category=Lifestyle' OR 1=1--
```

9. Send the modified request.
10. Observe that 8 products are returned.

---

## 4. Impact

SQL injection can allow an attacker to manipulate database queries through application input.

Depending on the application's database permissions and implementation, SQL injection may potentially lead to:

* Unauthorized data retrieval
* Bypass of application filtering
* Exposure of sensitive database information
* Further database compromise

**Demonstrated impact in this lab:** The application's intended category filtering was bypassed and additional products were returned.

---

## 5. Evidence Screenshots

**Screenshot 1:** `SQLi_01_baseline_3_products.png`
Shows the normal request and the 3-product result.

**Screenshot 2:** `SQLi_02_injection_8_products.png`
Shows the modified request and the 8-product result.

Session cookies, authentication tokens, and other sensitive values were blurred before using the screenshots as portfolio evidence.

---

## 6. Remediation

The application should:

1. Use **parameterized queries / prepared statements** instead of dynamically constructing SQL queries from user input.
2. Perform appropriate **server-side input validation**.
3. Use database accounts with the **minimum required privileges**.
4. Avoid exposing detailed database errors to users.
5. Implement appropriate security testing as part of the development lifecycle.

---

## 7. Security Conclusion

The authorized lab assessment successfully demonstrated SQL injection through the `category` parameter.

The vulnerability was confirmed by comparing a baseline request with a controlled modified request and observing a change in application behavior from **3 products to 8 products**.

This finding demonstrates the importance of validating and safely handling user-controlled input before it reaches database queries.
