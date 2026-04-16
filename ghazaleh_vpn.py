# ============================================================
# VPN Configuration Exposure Check
# ============================================================

import urllib.request

target = "http://vpn.0x10.cloud/client.ovpn"

print("=" * 55)
print("VPN Configuration Exposure Check")
print("=" * 55)

try:
    response = urllib.request.urlopen(target, timeout=5)

    print("\nTarget:", target)
    print("[!] Vulnerability Found")
    print("VPN configuration file is publicly accessible.")

    content = response.read().decode("utf-8", errors="ignore")

    if "remote" in content:
        print("- VPN server details exposed")

    if "route" in content:
        print("- Internal network routes exposed")

    if "BEGIN CERTIFICATE" in content:
        print("- Certificate data included (high risk)")

    print("\nImpact:")
    print("Attacker may gain access to internal network via VPN.")

except Exception:
    print("\n[OK] VPN configuration file not accessible.")

print("\n" + "=" * 55)