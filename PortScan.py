from Colors import Colors
import socket
import nmap
import xml.etree.ElementTree


class PortScan:
    def __init__(self, target):
        self.target = target
        
    def nmapScan(self, argument):
        print(f"{Colors.PURPLE}[*] Trying portscan{Colors.DEFAULT}")
        print(f"{Colors.BLUE}[-]\tport\tstate\tservice{Colors.DEFAULT}")
        
        try:
            nm = nmap.PortScanner()
            
            host = self.target
            portRange = "1-1024"
            
            nm.scan(host, portRange, arguments=argument)
            
            for host in nm.all_hosts():
                if nm[host].state() == "down":
                    print(f"{Colors.YELLOW}[!] Non-existent or inactive host{Colors.DEFAULT}")
                else:
                    for proto in nm[host].all_protocols():
                        print(f'[!] Protocol : {proto}')	
                        lport = nm[host][proto].keys()
                        for port in lport:
                            state = nm[host][proto][port]['state']
                            print(state)
                            service = nm[host][proto][port]['name']
                            self.formatResponse(port, state, service)
            
        except xml.etree.ElementTree.ParseError:
                print(f"{Colors.YELLOW}[!] Permission error: running as user{Colors.DEFAULT}\n\n")
        except nmap.PortScannerError:
                print(f"{Colors.YELLOW}[!] Permission error: running as user{Colors.DEFAULT}\n\n")
            
    def formatResponse(self, port, status, service):
        print(f"{Colors.GREEN}[+]\t{Colors.DEFAULT}{port}\t{Colors.GREEN}{status}{Colors.DEFAULT}\t{service}")