import socket

hostname = socket.gethostname()
local_ip = socket.gethostbyname(hostname)
google_ip = socket.gethostbyname("google.com")

google_hostname = socket.gethostbyaddr(google_ip)

print("Hostname:", hostname)
print("Local IP:", local_ip)
print("Google IP:", google_ip)
print("Reverse DNS:", google_hostname[0])