from Banner import Banner
from CrtScan import CrtScan    
from PortScan import PortScan
from SearchDirectory import SearchDirectory


def main(target, wordlist):    
    banner = Banner()
    banner.show()
    
    try:
        # certificate transparency
        crtScan = CrtScan(target)
        crtScan.get()
        
        # portscan
        portScan = PortScan(target)
        portScan.nmapScan("-sS")
        
        # directory bruteforce
        searchDirectory = SearchDirectory(target, wordlist)
        searchDirectory.get()
    except Exception as error:
        print(f"Unexpected error: {error}")