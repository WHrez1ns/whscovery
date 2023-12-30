from Colors import Colors
import socket


class PortScan:
    def __init__(self, target, ports):
        self.target = target
        self.ports = ports
    
    def simpleScanPort(self):
        print(f"{Colors.PURPLE}[*] Trying simple portscan{Colors.DEFAULT}")
        print(f"{Colors.BLUE}[-]\tport\tstatus{Colors.DEFAULT}")
        
        try:
            for port in self.ports:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.05)
                resp = client.connect_ex((self.target, port))
                self.formatResponse(port, resp)
            print("\n")
        except Exception as error:
            print(f"{Colors.YELLOW}[!] Simple portscan error: {error}{Colors.DEFAULT}\n")
            
    def formatResponse(self, port, status):
        if status == 0:
            print(f"{Colors.GREEN}[+]\t{Colors.DEFAULT}{port}\t{Colors.GREEN}OPEN{Colors.DEFAULT}")