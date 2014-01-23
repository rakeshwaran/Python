
import socket 
host = '127.0.0.1' 
port = 8111 
size = 1024 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host,port)) 
s.send('Helloworld') 
data = s.recv(size) 
s.close() 
print 'Received:', data
