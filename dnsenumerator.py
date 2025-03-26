import dns.resolver

def dns_enumerator(domain):
    try:
        answers = dns.resolver.resolve(domain, 'A')
        for rdata in answers:
            print(f"IP Address: {rdata}")
    except dns.resolver.NoAnswer:
        print("No IP addresses found")
