                      [![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org)
                      [![Hacking](https://img.shields.io/badge/Hacking-111111?style=flat-square&logo=hackthebox&logoColor=red)](#)
                      [![OSINT](https://img.shields.io/badge/OSINT-0052CC?style=flat-square)](#)
                      [![Security](https://img.shields.io/badge/Security-0A84FF?style=flat-square&logo=shield&logoColor=white)](#)



OSINT SUITE v2.0
Open-source intelligence (OSINT) gathering tool developed in Python by synq1xxs. It automates queries regarding email addresses, domains, IP addresses, usernames, and phone numbers.

Features
Email OSINT: Checks security breaches via HaveIBeenPwned, reputation via EmailRep.io, and verification via Hunter.io.

Domain OSINT: Extracts WHOIS records and resolves DNS records (A, MX).

IP OSINT: Geolocation via ip-api.com and abuse report checking via AbuseIPDB.

Username OSINT: Checks username availability across 12 social platforms sequentially.

Phone OSINT: Validates structure, country, and carrier information using Numverify and Veriphone APIs.

Requirements
The script requires Python 3 and the following external dependencies:

requests

python-whois

dnspython

Installation
Clone the repository or download the script.

Install the required dependencies using pip:

Bash
pip install requests python-whois dnspython
Usage
Run the main script from the terminal:

Bash
python Osynt.py
The program displays an interactive command-line menu. Select the desired option and input the target when prompted. Some modules optionally accept API keys (Hunter.io, AbuseIPDB, Numverify) to extend the results.
