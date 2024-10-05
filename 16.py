import socket 

def handle_client(conn,addr):
    while True:
        data=conn.recv(1024)
        if not data:
            break
        conn.send(data.upper().encode())

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.bind(('localhost',12345))
sock.listen()

while True:
    conn,addr = sock.accept()
    print(f"connected by: {addr}")
    handle_client(conn, addr)
    conn.close()