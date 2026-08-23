import socket

target = input("Enter IP address: ")

start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

ports = range(start_port, end_port + 1)

services = {
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    8080: "HTTP-ALT"
}

open_ports = []

print("\nScanning:", target)
print("=" * 30)

for port in ports:

    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)

    result = scanner.connect_ex((target, port))

    if result == 0:
        open_ports.append(port)
        print(f"TCP Port {port}: OPEN | Service: {services.get(port, 'Unknown')}")

    scanner.close()

print("\nScan Complete")
print("Open Ports:", len(open_ports))