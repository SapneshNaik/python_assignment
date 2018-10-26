# echo_client.py
import socket

port = 12345                   # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', port))

msg = input("Enter msg:\n")

s.sendall(msg.encode())

data = s.recv(1024)
s.close()
print(data.decode())