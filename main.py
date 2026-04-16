# ============================================================
#  COMP2152 — Term Project: CTF Bug Bounty
#  Main Runner — Runs all vulnerability check scripts
# ============================================================

import subprocess
import sys
import os

scripts = [
    "ghazaleh_upload.py",
    "mina_internal_dns_records_exposure.py",
    "Ashkan_backup_server.py",
    " Kamand_login.py",
   
]

if __name__ == "__main__":
    # Run scripts from the same directory as main.py
    script_dir = os.path.dirname(os.path.abspath(__file__))

    print("\n" + "=" * 50)
    print("  COMP2152 — Bug Bounty Scanner")
    print("  Running all vulnerability checks...")
    print("=" * 50, flush=True)

    for script in scripts:
        print(f"\n>>> Running {script}...\n", flush=True)
        script_path = os.path.join(script_dir, script)
        subprocess.run([sys.executable, script_path])

    print("\n" + "=" * 50)
    print("  All checks complete.")
    print("=" * 50 + "\n")
