import requests

def subdomain_scanner(domain, subdomains):
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                print(f"Subdomain found: {url}")
        except requests.exceptions.RequestException:
            pass
