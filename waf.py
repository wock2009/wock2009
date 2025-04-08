import requests as r
from colorama import init as i, Fore as f
i(autoreset=True)
def a(b):
    try:
        c=r.get(b)
        d={("X-Sucuri-ID"):("Sucuri WAF"),("CF-RAY"):("Cloudflare"),("Server"):("nginx"),("X-Content-Type-Options"):("nosniff"),("X-Frame-Options"):("DENY")}
        print(f.CYAN + "Response headers for " + b + ":\n")
        for e,g in c.headers.items():
            print(f.YELLOW + e + ":" + g)
        print(f.MAGENTA + "\nWAF SCAN INFO")
        for e,g in d.items():
            if e in c.headers:
                print(f.GREEN + "WAF detected" + e + "=" + c.headers[e])
                return True
        print(f.RED + "No WAF detected")
        return False
    except r.RequestException as h:
        print(f.RED + "WARNING error checking" + str(h))
        return False
b=input(f.CYAN + "Enter url to scan> ")
if a(b):
    print(f.GREEN + "The website " + b + " use WAF")
else:
    print(f.RED + "The website " + b + " does not use WAF")