import sys
from Banner import Banner
from CrtScan import CrtScan                                        
    
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
            print("""Usage: main.py <target> <options>
        
All flags:
                -h, --help: All flags for use
                -c, --certificate: Certificate transparency 
                for subdomains/domain discovery""")
        # help
        elif sys.argv[1] == "--help" or sys.argv[1] == "-h":
            print("""All flags:
                -h, --help: All flags for use
                -c, --certificate: Certificate transparency 
                for subdomains/domain discovery""")
        # certificate transparency
        elif sys.argv[2] == "--certificate" or sys.argv[2] == "-c":
            try: 
                crtScan = CrtScan(sys.argv[1])
                crtScan.get()
            except IndexError:
                print("Usage: main.py <target> -c")
        # default output
        else:
            print("Usage: main.py <target> <options>")
    except Exception as error:
        print(error)
        
        
if __name__ == "__main__":
    main()