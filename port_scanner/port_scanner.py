import socket

target = input("Enter IP address: ")

port = int(input("Enter port number: "))

scanner = socket.socket()

result = scanner.connect_ex((target, port))

if result == 0:
    print("Port is open")
else:
    print("Port is closed")

scanner.close()