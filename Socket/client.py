from socket import *
s = socket()
port = 2345
s.connect(('localhost', port))
print(s.recv(1024))
s.close()
