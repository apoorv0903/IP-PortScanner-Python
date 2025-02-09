import socket
from IPy import IP


def scan(target):
    converted_ip = check_ip(target)
    print('\n' + '[-_0 scanning Target] ' + str(target))
    for port in range(1,100):
        scan_port(converted_ip, port)


def check_ip(ip):
    try:
        IP(ip)
        return(ip)
    except ValueError:
        return socket.gethostbyname(ip)


def get_banner(s):
    return s.recv(1024)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.settimeout(1.25)
        sock.connect((ipaddress, port))
        try:
            banner = get_banner(sock)
            print('[+] Open port ' + str(port) + ' : ' + str(banner.decode().strip('\n'))) 
        except:
            print('[+] Open port ' + str(port))

    except:
        pass
        #print('[-] Port ' + str(port) + ' is closed')


targets = input('[+] Enter the Target(s) to Scan(split multiple targets with comma,): ')

if ',' in targets:
    for ip_add in targets.split(','):
        scan(ip_add.strip(' '))

else:
    scan(targets)



