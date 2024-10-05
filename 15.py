import socket

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

sock.bind(('localhost',12345))

sock.listen()

conn,addr=sock.accept()

data=1024
conn.send(data.encode())
data_received = conn.recv(1024)

conn.close()
sock.close()
