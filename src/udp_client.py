import socket

target_host = "127.0.0.1"
target_port = 80

# create a socket object
#   AF_INET tells that you'll use a standard IPV4 address or hostname
#   SOCK_DGRAM means the this will be a UDP client
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Obs.: Because UDP is a connectionless protocol, there is no call to connect() here

# send some data
client.sendto("AAABBBCCC", (target_host, target_port))

# receive some data
data, add = client.recvfrom(4096)

print data
