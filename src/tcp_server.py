import socket
import threading

target_host = "127.0.0.1"
target_port = 9999

# Server TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((target_host, target_port))

# allows only 5 connections at a time
server.listen(5)


def handle_client(client):
    data = client.recvfrom(4096)
    print "[*] Data received: %s" % repr(data)
    client.send("ACK!")
    client.close()


# To-Do: Add timeout to break the loop below
while True:
    client, address = server.accept()
    print "[*] Listening at address %s:%d" % (address[0], address[1]) # host, port
    client_thread = threading.Thread(target=handle_client, args=(client,))
    client_thread.start()

# Does it make sense put it here at the end?
server.close()
