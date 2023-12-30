from Banner import Banner
from CrtScan import CrtScan    
from PortScan import PortScan    
from ReverseShellGenerator import ReverseShellGenerator


def main(target):    
    banner = Banner()
    banner.show()
    
    try:
        crtScan = CrtScan(target)
        crtScan.get()
        
        defaultWordlist = [ 21, 22, 80, 8080, 443, 3306 ]
        portScan = PortScan(target, defaultWordlist)
        portScan.simpleScanPort()
        
        reverseShellGenerator = ReverseShellGenerator(target)
        reverseShellGenerator.generate()
        
    except Exception as error:
        print(f"Unexpected error: {error}")