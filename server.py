import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '0.0.0.0'
port = 8080
s.bind((socket.gethostname(), 80))
s.listen(5)
print(host)
print("waiting for incoming connections... ")
conn, addr = s.accept()
print(addr, "Has connected to the server")
dataTest = ""
while True:
    
    data = conn.recv(1024)
    print(data.decode())