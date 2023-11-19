import socket
target = input("Enter the host to be scanned: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Hostname could not be resolved.")
    exit()
socket.setdefaulttimeout(1)  # 1 second
for port in range(start_port, end_port + 1):
    # See next steps for what goes inside the loop

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = s.connect_ex((target_ip, port))
    if result == 0:
        print(f"Port {port} is open!")
    s.close()

try:
    # Loop and check port status (Steps 8 & 9)
except KeyboardInterrupt:
    print("\\nExiting program.")
    exit()
except socket.error:
    print("Couldn't connect to server.")
    exit()
