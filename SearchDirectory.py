from Colors import Colors
import requests


class SearchDirectory:
    def __init__(self, target, wl):
        self.target = target
        self.wl = wl
        
    def get(self):
        print(f"{Colors.RED}[*] Trying directory bruteforce{Colors.DEFAULT}")
        print(f"{Colors.BLUE}[-]\tdirectory\tcode\tstatus{Colors.DEFAULT}")
        
        try:
            fileDirectoryList = []
            with open(f"{self.wl}", "r") as wordlist:
                fileDirectoryList = wordlist.readlines()
            
            for item in fileDirectoryList:
                endpoint = f"https://{self.target}/{str.strip(item)}"
                resp = requests.get(endpoint)
                self.formatResponse(resp.status_code, str.strip(item))
            print("\n")  
        except Exception as error:
            print(f"{Colors.YELLOW}[!] Directory bruteforce error: {error}{Colors.DEFAULT}\n")
        
    def formatResponse(self, statusCode, item):
        if statusCode == 200:
            print(f"{Colors.GREEN}[+]\t{Colors.DEFAULT}/{item}\t\t{Colors.GREEN}{statusCode}\tSucess{Colors.DEFAULT}")
        elif statusCode == 403 or statusCode == 401:
            print(f"{Colors.GREEN}[+]\t{Colors.DEFAULT}/{item}\t\t{Colors.REDB}{statusCode}\tForbidden{Colors.DEFAULT}")
        elif statusCode < 400 and statusCode >= 300:
            print(f"{Colors.GREEN}[+]\t{Colors.DEFAULT}/{item}\t\t{Colors.YELLOWB}{statusCode}\tRedirection{Colors.DEFAULT}")
        elif statusCode >= 500:
            print(f"{Colors.GREEN}[+]\t{Colors.DEFAULT}/{item}\t\t{Colors.REDB}{statusCode}\tServer Error{Colors.DEFAULT}")
        else:
            pass