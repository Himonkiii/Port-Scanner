# 🔍 Python Port Scanner

A fast, multithreaded port scanner built from scratch in Python.
Scans any target for open ports, grabs service banners, and identifies what's running.

---

##  Features

-  Multithreaded — scans 1000 ports in under 3 seconds
-  Banner grabbing — detects software and versions on open ports
-  Service identification — recognizes SSH, HTTP, FTP, MySQL, RDP and more
-  Works on any IP address or domain name
-  Clean output with scan duration and summary

---

## 📸 Example Output
```
==================================================
Target:   scanme.nmap.org (45.33.32.156)
Ports:    1 to 1000
Started:  2026-03-09 01:20:43
==================================================
[OPEN] Port 22  (SSH)  ---> SSH-2.0-OpenSSH_6.6.1p1 Ubuntu
[OPEN] Port 80  (HTTP) ---> Server: Apache/2.4.7 (Ubuntu)
==================================================
Scan complete!
Open ports:   [22, 80]
Total open:   2
Time taken:   2 seconds
==================================================
```

---

##  How to Use
1. Clone the repo
```
git clone https://github.com/Himonkiii/Port-Scanner.git
```
2. Run the script
```
python port_scanner.py
```
3. Enter when prompted
```
Enter target IP or website: scanme.nmap.org
Enter start port: 1
Enter end port: 1000
```
---
##  What I Learned Building This
- How TCP sockets work under the hood
- What port scanning actually does (same concept as Nmap)
- How service banners reveal software versions
- Python threading and race condition handling with locks
- Why open ports matter in cybersecurity and pentesting
---
##  Built With
- Python 3
- socket — network connections
- threading — parallel scanning
- datetime — scan timing
---
##  LEGAL DISCLAIMER ##

Only scan targets you have permission to scan.
`scanme.nmap.org` is provided by Nmap specifically for practice scanning.
Unauthorized scanning is illegal.

---

##  Author

**Himank Bhandari**
CSE Student | Cybersecurity Enthusiast
