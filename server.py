import socket 

host = '127.0.0.1' 
port = 8111 
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
while 1: 
    client, address = s.accept()
    data = client.recv(size) 
    if data: 
        client.send(data) 
    client.close()

