from Colors import Colors
import socket

class PortScan:
    def __init__(self, target, ports):
        self.target = target
        self.ports = ports
    
    def simpleScanPort(self):
        # Simple Portscan
        print(f"{Colors.CIAN}[*] Trying simple portscan{Colors.DEFAULT}")
        
        try:
            for port in self.ports:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.settimeout(0.05)
                resp = client.connect_ex((self.target, port))
                self.formatResponse(port, resp)
        except:
            print(f"{Colors.YELLOW}Error, something is wrong.{Colors.DEFAULT}")
            
    def formatResponse(self, port, status):
        if status == 0:
            print(f"[+] Port {port}{Colors.GREEN}  OPEN {Colors.DEFAULT} in {self.target}")
        else:
            print(f"[+] Port {port}{Colors.RED}  CLOSED {Colors.DEFAULT} in {self.target}")