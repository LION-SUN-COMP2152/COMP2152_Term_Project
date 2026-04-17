# COMP2152 — Term Project: CTF Bug Bounty

## Team Name

<!-- Replace with your team name -->

Team Lion and Sun

## Team Members

| Member             | Vulnerability Found | Branch Name |
| ------------------ | ------------------- | ----------- |
| Ghazaleh AzimiKorf | upload.0x10.cloud   | Ghazaleh    |
| Mina Fahim         | dns.0x10.cloud      | mina_fahim  |
| Kiana Sepasian     | api.0x10.cloud      | Kiana       |
| Kamand Rosrami     | login.0x10.cloud    | Kamand      |
| Ashkan pazaj       | backup.0x10.cloud   | Ashkan      |

## Videos

Each team member records a short video (max 3 minutes) explaining their vulnerability. Add your YouTube links below:

- Member 1 (Ghazaleh AzimIKorf) : https://youtu.be/3YPUAFF3crQ?si=SYEkcHvzDeu-FOKt
- Member 2 (Mina Fahim): https://youtu.be/Ef-EFDNpns8
- Member 3 (Kiana Sepasian): https://youtu.be/w40Y22gmvuQ
- Member 4 (Kamand Rosrami): https://youtu.be/bErkrb6A8go
- Member 5 (Ashkan Pazj): https://youtu.be/ASlvKn2BQUU

## Target

- Server: `0x10.cloud` and its subdomains
- Submission: http://submit.0x10.cloud
- Leaderboard: http://ranking.0x10.cloud

## Important: Rate Limit

The server allows **10 requests per second** per IP address. If you send requests too fast, you will get blocked (HTTP 429). Add a small delay between requests:

```python
import time
time.sleep(0.15)  # wait 150ms between requests
```

## Getting Started

1. Look at the three example scripts:
   - `example_http_check.py` — checks if a site uses HTTPS (uses `urllib`)
   - `example_port_check.py` — checks if a port is open (uses `socket`)
   - `example_header_check.py` — reads HTTP response headers for info leaks (uses `urllib`)
2. Run all examples: `python3 main.py`
3. Create your own branch: `git checkout -b your_vuln_name`
4. Write a Python script that finds and demonstrates a vulnerability
5. Submit your finding at http://submit.0x10.cloud
6. Merge your branch into master when done

## Rules

- **Python standard library only** — `socket`, `urllib`, `ssl`, `json`, `base64`, `time`. No pip packages.
- **Only scan `*.0x10.cloud`** — do not scan any other domain.
- **Respect the rate limit** — 10 requests/second max.
