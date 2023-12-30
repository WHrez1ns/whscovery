from Colors import Colors
import requests


class CrtScan:
    def __init__(self, target):
        self.target = target 
    
    def get(self):
        print(f"{Colors.PURPLE}[*] Trying certificate transparency{Colors.DEFAULT}")

        try:
            resp = requests.get(f"https://crt.sh?q={self.target}&output=json")
            json = resp.json()
            self.formatResponse(json)
            print("\n")
        except Exception as error:
            print(f"{Colors.YELLOW}[!] Certificate transparency error: {error}{Colors.DEFAULT}\n")
    
    def formatResponse(self, json):
        subdomains = []
        for dic in json:
            subdomain = dic["name_value"].replace("\n", ", ")
            # domain = dic["common_name"]
            
            subdomains.append(f"{Colors.GREEN}[+]\t{Colors.DEFAULT}subdomain(s):\t{Colors.GREEN}{subdomain}{Colors.DEFAULT}")
        
        noRepeatSubdomains = set(subdomains)
        subdomainsList = list(noRepeatSubdomains)
        
        for subdomain in subdomainsList:
            print(subdomain) if not "*" in subdomain else "" 
            # print(subdomain)