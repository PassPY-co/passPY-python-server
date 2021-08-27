import socket
s = socket.socket()
host = '127.0.0.1'
port = 8080
s.connect((host, port))
print("connecting...")
while True:
    text = input("message:").encode()
    s.send(text)