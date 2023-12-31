from Banner import Banner
from CrtScan import CrtScan    
from PortScan import PortScan    
from ReverseShellGenerator import ReverseShellGenerator
from SearchDirectory import SearchDirectory


def main(target):    
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
        searchDirectory = SearchDirectory(target)
        searchDirectory.get()
        
        # reverse shell generator
        # reverseShellGenerator = ReverseShellGenerator()
        # reverseShellGenerator.generate()
    except Exception as error:
        print(f"Unexpected error: {error}")