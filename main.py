import sys
from Banner import Banner
from CrtScan import CrtScan    
from Colors import Colors   
from PortScan import PortScan                                 
    
def main():
    try:
        # banner        
        banner = Banner()
        banner.show()

        # no arguments
        if len(sys.argv) < 2:
            print("Usage: main.py --help")
            sys.exit(1)
        elif len(sys.argv) == 2 and sys.argv[1] != "--help" and sys.argv[1] != "-h":
            print(f"""Usage: main.py <target> <options>
        
All flags:
                {Colors.YELLOW}-h, --help{Colors.DEFAULT}: All flags for use
        
        Options:
                {Colors.GREEN}-C, --complete{Colors.DEFAULT}: Complete enumeration        
                {Colors.GREEN}-c, --certificate{Colors.DEFAULT}: Certificate transparency 
                for subdomains/domain discovery
                {Colors.GREEN}-p, --port{Colors.DEFAULT}: Simple Portscan""")
        # help
        elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print(f"""All flags:
                {Colors.YELLOW}-h, --help{Colors.DEFAULT}: All flags for use
        
        Options:
                {Colors.GREEN}-C, --complete{Colors.DEFAULT}: Complete enumeration        
                {Colors.GREEN}-c, --certificate{Colors.DEFAULT}: Certificate transparency 
                for subdomains/domain discovery
                {Colors.GREEN}-p, --port{Colors.DEFAULT}: Simple Portscan""")
        
        # certificate transparency
        elif sys.argv[2] == "--certificate" or sys.argv[2] == "-c":
            try: 
                crtScan = CrtScan(sys.argv[1])
                crtScan.get()
            except IndexError:
                print("Usage: main.py <target> -c")
        
        # portscan
        elif sys.argv[2] == "--port" or sys.argv[2] == "-p":
            try:
                defaultWordlist = [ 21, 22, 80, 8080, 443, 3306 ]
                
                portScan = PortScan(sys.argv[1], defaultWordlist)
                portScan.simpleScanPort()
            except:
                print("Usage: main.py <target> -p")
        
        # complete scan   
        elif sys.argv[2] == "--complete" or sys.argv[2] == "-C":
            try:
                crtScan = CrtScan(sys.argv[1])
                crtScan.get()
                print("\n")
                
                defaultWordlist = [ 21, 22, 80, 8080, 443, 3306 ]
                portScan = PortScan(sys.argv[1], defaultWordlist)
                portScan.simpleScanPort()
                print("\n")
            except:
                print("Usage: main.py <target> --complete")
            
        # default output
        else:
            print("Usage: main.py <target> <options>")
    except Exception as error:
        print(error)
        
        
if __name__ == "__main__":
    main()