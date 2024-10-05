import socket 

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(('localhost',12345))

message="HEllo World!!"
sock.send(message.encode())

data=sock.recv(1024)
print(data.decode())

sock.close()
