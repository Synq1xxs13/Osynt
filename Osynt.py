import os
import sys
import time
import json
import requests
import whois
import dns.resolver
from datetime import datetime

def limpiar():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    limpiar()
    print("")
    print("")
    print("    ▒█████    ██████▓██   ██▓ ███▄    █ ▄▄▄█████▓")
    print("    ▒██▒  ██▒▒██    ▒ ▒██  ██▒ ██ ▀█   █ ▓  ██▒ ▓▒")
    print("    ▒██░  ██▒░ ▓██▄    ▒██ ██░▓██  ▀█ ██▒▒ ▓██░ ▒░")
    print("    ▒██   ██░  ▒   ██▒ ░ ▐██▓░▓██▒  ▐▌██▒░ ▓██▓ ░ ")
    print("    ░ ████▓▒░▒██████▒▒ ░ ██▒▓▒░▒██░   ▓██░  ▒██▒ ░ ")
    print("    ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░  ██▒▒▒ ░ ▒░   ▒ ▒   ▒ ░░   ")
    print("      ░ ▒ ▒░ ░ ░▒  ░ ░▓██ ░▒░ ░ ░░   ░ ▒░    ░    ")
    print("    ░ ░ ░ ▒  ░  ░  ░  ▒ ▒ ░░     ░   ░ ░   ░      ")
    print("        ░ ░        ░  ░ ░              ░          ")
    print("                      ░ ░                         ")
    print("")
    print("    By synq1xxs")
    print("")
    print("    OSINT SUITE v2.0")
    print("    " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("")
    print("    [1]  Email OSINT")
    print("    [2]  Domain OSINT")
    print("    [3]  IP OSINT")
    print("    [4]  Username OSINT")
    print("    [5]  Phone OSINT")
    print("    [6]  Full Report")
    print("    [7]  Exit")
    print("")

def email_osint():
    limpiar()
    print("")
    print("    EMAIL OSINT")
    print("    " + "-" * 40)
    
    email = input("    target email: ")
    if not email:
        return
    
    print("    " + "-" * 40)
    print("    scanning...")
    print("")
    print("    email: " + email)
    print("    domain: " + (email.split('@')[1] if '@' in email else 'N/A'))
    print("")
    
    print("    [1] HaveIBeenPwned (no API key required)")
    try:
        resp = requests.get(f"https://api.haveibeenpwned.com/api/v3/breachedaccount/{email}", timeout=10)
        if resp.status_code == 200:
            breaches = resp.json()
            print("    breaches found: " + str(len(breaches)))
            for b in breaches:
                print("      - " + b['Name'])
        elif resp.status_code == 404:
            print("    no public breaches found")
        else:
            print("    API error: " + str(resp.status_code))
    except:
        print("    error connecting to HaveIBeenPwned")
    
    print("")
    print("    [2] EmailRep.io (no API key required)")
    try:
        resp = requests.get(f"https://api.emailrep.io/{email}", timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            print("    reputation: " + str(data.get('reputation', 'N/A')))
            print("    suspicious: " + str(data.get('suspicious', False)))
            print("    references: " + str(data.get('references', 0)))
            if data.get('details'):
                print("    details:")
                for k, v in data.get('details', {}).items():
                    print("      " + k + ": " + str(v))
        else:
            print("    emailrep.io: no data")
    except:
        print("    emailrep.io: error")
    
    print("")
    print("    [3] Hunter.io (requires API key)")
    api_key = input("    Hunter.io API Key (leave empty to skip): ")
    if api_key:
        try:
            domain = email.split('@')[1]
            resp = requests.get(f"https://api.hunter.io/v2/email-verifier?email={email}&api_key={api_key}", timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                if data.get('data'):
                    print("    status: " + str(data['data'].get('status', 'N/A')))
                    print("    result: " + str(data['data'].get('result', 'N/A')))
                    print("    score: " + str(data['data'].get('score', 'N/A')))
                else:
                    print("    no data")
            else:
                print("    Hunter.io error: " + str(resp.status_code))
        except:
            print("    Hunter.io: error")
    
    print("")
    input("    press Enter to continue...")

def dominio_osint():
    limpiar()
    print("")
    print("    DOMAIN OSINT")
    print("    " + "-" * 40)
    dominio = input("    target domain: ")
    if not dominio:
        return
    print("    " + "-" * 40)
    print("    fetching WHOIS + DNS...")
    print("")
    try:
        w = whois.whois(dominio)
        print("    WHOIS:")
        print("      registrar: " + str(w.name if w.name else 'N/A'))
        print("      email: " + str(w.emails if w.emails else 'N/A'))
        print("      created: " + str(w.creation_date if w.creation_date else 'N/A'))
        print("      expires: " + str(w.expiration_date if w.expiration_date else 'N/A'))
        print("      nameservers: " + str(w.name_servers if w.name_servers else 'N/A'))
    except Exception as e:
        print("    WHOIS error: " + str(e))
    print("")
    try:
        answers = dns.resolver.resolve(dominio, 'A')
        print("    DNS A records:")
        for r in answers:
            print("      - " + r.address)
    except:
        print("    no A records found")
    print("")
    try:
        answers = dns.resolver.resolve(dominio, 'MX')
        print("    DNS MX records:")
        for r in answers:
            print("      - " + str(r.exchange) + " (priority: " + str(r.preference) + ")")
    except:
        print("    no MX records found")
    print("")
    input("    press Enter to continue...")

def ip_osint():
    limpiar()
    print("")
    print("    IP OSINT")
    print("    " + "-" * 40)
    ip = input("    target IP: ")
    if not ip:
        return
    print("    " + "-" * 40)
    print("    geolocating...")
    print("")
    try:
        resp = requests.get(f"http://ip-api.com/json/{ip}", timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data['status'] == 'success':
                print("    IP: " + data['query'])
                print("    country: " + data['country'] + " (" + data['countryCode'] + ")")
                print("    region: " + data['regionName'])
                print("    city: " + data['city'])
                print("    ISP: " + data['isp'])
                print("    coordinates: " + str(data['lat']) + ", " + str(data['lon']))
                print("    map: https://maps.google.com/?q=" + str(data['lat']) + "," + str(data['lon']))
            else:
                print("    IP not found")
        else:
            print("    API error")
    except Exception as e:
        print("    error: " + str(e))
    
    print("")
    print("    [1] AbuseIPDB (requires API key)")
    api_key = input("    AbuseIPDB API Key (leave empty to skip): ")
    if api_key:
        try:
            resp = requests.get(f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip}", 
                              headers={'Key': api_key}, timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                if data.get('data'):
                    print("    abuse score: " + str(data['data'].get('abuseConfidenceScore', 'N/A')))
                    print("    total reports: " + str(data['data'].get('totalReports', 0)))
                    print("    country: " + str(data['data'].get('countryCode', 'N/A')))
                    print("    last reported: " + str(data['data'].get('lastReportedAt', 'N/A')))
                else:
                    print("    no data")
            else:
                print("    AbuseIPDB error: " + str(resp.status_code))
        except:
            print("    AbuseIPDB: error")
    
    print("")
    input("    press Enter to continue...")

def usuario_osint():
    limpiar()
    print("")
    print("    USERNAME OSINT")
    print("    " + "-" * 40)
    usuario = input("    target username: ")
    if not usuario:
        return
    print("    " + "-" * 40)
    print("    checking social media...")
    print("")
    
    redes = {
        'Instagram': "https://www.instagram.com/" + usuario,
        'Twitter': "https://twitter.com/" + usuario,
        'Facebook': "https://www.facebook.com/" + usuario,
        'TikTok': "https://www.tiktok.com/@" + usuario,
        'GitHub': "https://github.com/" + usuario,
        'Reddit': "https://www.reddit.com/user/" + usuario,
        'YouTube': "https://www.youtube.com/@" + usuario,
        'Telegram': "https://t.me/" + usuario,
        'Tumblr': "https://" + usuario + ".tumblr.com",
        'Pinterest': "https://www.pinterest.com/" + usuario,
        'Spotify': "https://open.spotify.com/user/" + usuario,
        'Twitch': "https://www.twitch.tv/" + usuario
    }
    
    for red, url in redes.items():
        try:
            resp = requests.head(url, timeout=5)
            if resp.status_code == 200:
                print("    + " + red + ": " + url)
            else:
                print("    - " + red + ": not found")
        except:
            print("    ? " + red + ": no response")
        time.sleep(0.2)
    print("")
    input("    press Enter to continue...")

def telefono_osint():
    limpiar()
    print("")
    print("    PHONE OSINT")
    print("    " + "-" * 40)
    telefono = input("    target phone (international): ")
    if not telefono:
        return
    print("    " + "-" * 40)
    print("    validating...")
    print("")
    print("    number: " + telefono)
    print("")
    
    print("    [1] Numverify (requires API key)")
    api_key = input("    Numverify API Key (get free at https://numverify.com): ")
    if api_key:
        try:
            resp = requests.get(f"http://apilayer.net/api/validate?access_key={api_key}&number={telefono}", timeout=10)
            if resp.status_code == 200:
                data = resp.json()
                if data.get('valid', False):
                    print("    valid: True")
                    print("    country: " + data.get('country_name', 'N/A'))
                    print("    carrier: " + data.get('carrier', 'N/A'))
                    print("    line: " + data.get('line_type', 'N/A'))
                    print("    location: " + data.get('location', 'N/A'))
                else:
                    print("    valid: False")
            else:
                print("    Numverify error: " + str(resp.status_code))
        except Exception as e:
            print("    Numverify error: " + str(e))
    
    print("")
    print("    [2] Phone validation without API (limited)")
    try:
        resp = requests.get(f"https://api.veriphone.io/v2/verify?phone={telefono}", timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('phone_valid', False):
                print("    valid: True")
                print("    country: " + data.get('country_name', 'N/A'))
                print("    carrier: " + data.get('carrier', 'N/A'))
            else:
                print("    valid: False")
        else:
            print("    Veriphone: error")
    except:
        print("    Veriphone: error")
    
    print("")
    input("    press Enter to continue...")

def reporte_completo():
    limpiar()
    print("")
    print("    FULL REPORT")
    print("    " + "-" * 40)
    print("    this module will generate a unified JSON report")
    print("    containing all collected intelligence.")
    print("")
    print("    module under development")
    print("")
    input("    press Enter to continue...")

def main():
    while True:
        menu()
        opcion = input("    select option: ")
        if opcion == "1":
            email_osint()
        elif opcion == "2":
            dominio_osint()
        elif opcion == "3":
            ip_osint()
        elif opcion == "4":
            usuario_osint()
        elif opcion == "5":
            telefono_osint()
        elif opcion == "6":
            reporte_completo()
        elif opcion == "7":
            limpiar()
            print("")
            print("    OSINT SUITE")
            print("    " + "-" * 40)
            print("    exiting...")
            print("")
            print("    By synq1xxs")
            print("")
            time.sleep(1)
            sys.exit()
        else:
            print("    invalid option")
            time.sleep(0.8)

if __name__ == "__main__":
    main()