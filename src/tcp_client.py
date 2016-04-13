import socket

target_host = "0.0.0.0"
target_port = 9999

# create a socket object
#   AF_INET tells that you'll use a standard IPV4 address or hostname
#   SOCK_STREAM means the this will be a TCP client
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send("""GET / HTTP/1.1
Host: google.com

""")

# receive some data
response = client.recv(4096)

print response
