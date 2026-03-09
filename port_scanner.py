import socket
import datetime
import threading
import sys

target = input("Enter target IP or website: ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

#resolve hostname to IP
try:
    ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Could not resolve hostname: " + target)
    sys.exit()

open_ports = []
lock = threading.Lock()

# ─── COMMON PORTS DICTIONARY ───
common_ports = {
    21:  "FTP",
    22:  "SSH",
    23:  "Telnet",
    25:  "SMTP",
    53:  "DNS",
    80:  "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
}

def grab_banner(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        sock.connect((ip, port))
        if port == 22 or port == 21 or port == 25:
            banner = sock.recv(1024).decode().strip()
        else:
            sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
            banner = sock.recv(1024).decode().strip()
            for line in banner.split("\n"):
                if "Server:" in line:
                    banner = line.strip()
                    break
        sock.close()
        return banner
    except:
        return ""

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        sock.close()

        if result == 0:
            banner = grab_banner(ip, port)
            # check if its a known port
            service = common_ports.get(port, "unknown service")
            with lock:
                open_ports.append(port)
                if banner:
                    print("[OPEN] Port " + str(port) + " (" + service + ") ---> " + banner)
                else:
                    print("[OPEN] Port " + str(port) + " (" + service + ")")
    except:
        pass

# ─── MAIN ───
print("=" * 50)
print("Target:   " + target + " (" + ip + ")")
print("Ports:    " + str(start_port) + " to " + str(end_port))
print("Started:  " + str(datetime.datetime.now()))
print("=" * 50)

start_time = datetime.datetime.now()
threads = []

for port in range(start_port, end_port + 1):
    thread = threading.Thread(target=scan_port, args=(port,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time = datetime.datetime.now()
duration = end_time - start_time

print("=" * 50)
print("Scan complete!")
print("Open ports:   " + str(sorted(open_ports)))
print("Total open:   " + str(len(open_ports)))
print("Time taken:   " + str(duration.seconds) + " seconds")
print("=" * 50)