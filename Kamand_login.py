"""
Author: Kamand Roastami 
Vulnerability: Authentication Endpoint Lacks Brute-Force Protection and Explicitly Allows Unlimited Login Attempts
Target: login.0x10.cloud
"""

import urllib.request
import urllib.parse
import urllib.error

target = "http://login.0x10.cloud/"

post_data = urllib.parse.urlencode({
    "username": "",
    "password": ""
}).encode("utf-8")

request = urllib.request.Request(target, data=post_data, method="POST")
request.add_header("Content-Type", "application/x-www-form-urlencoded")

print("=" * 80)
print("Authentication Endpoint Lacks Brute-Force Protection")
print("=" * 80)

try:
    response = urllib.request.urlopen(request, timeout=10)
    body = response.read().decode("utf-8", errors="ignore")

    print("Target:", target)
    print("HTTP Status:", response.status)
    print("Response:")
    print(body)
    print()

    normalized = body.replace(" ", "").lower()

    if '"attempts":"unlimited"' in normalized:
        print("[!] VULNERABILITY FOUND")
        print("The authentication endpoint explicitly indicates that login attempts are unlimited.")
        print("This suggests that failed login attempts are not meaningfully restricted.")
        print("Such behavior increases the risk of brute-force and credential-stuffing attacks.")
    else:
        print("[OK] No unlimited-attempt indicator was detected in the response.")

except urllib.error.HTTPError as e:
    error_body = ""
    try:
        error_body = e.read().decode("utf-8", errors="ignore")
    except Exception:
        pass

    print("HTTP Error:", e.code, e.reason)
    if error_body:
        print("Response Body:")
        print(error_body)

except urllib.error.URLError as e:
    print("URL Error:", e.reason)

except Exception as e:
    print("Error:", e)

print("=" * 80)