from Colors import Colors
import requests

class CrtScan:
    def __init__(self, target):
        self.target = target 
        
    def get(self):
        # Certificate Tranparency
        print(f"{Colors.CIAN}[*] Trying certificate transparency{Colors.DEFAULT}")

        resp = requests.get(f"https://crt.sh?q={self.target}&output=json")
        json = resp.json()
        self.formatResponse(json)
        
    def formatResponse(self, json):
        subdomains = []
        for dic in json:
            subdomain = dic["name_value"].replace("\n", ", ")
            domain = dic["common_name"]
            
            subdomains.append(f"[+] Found: {Colors.GREEN}{subdomain}{Colors.DEFAULT} in {domain}")
        
        noRepeatSubdomains = set(subdomains)
        subdomainsList = list(noRepeatSubdomains)
        
        for subdomain in subdomainsList:
            print(subdomain) # print(subdomain) if not "*" in subdomain else ""