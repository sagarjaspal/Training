from socket import *
s = socket()
host = gethostname()
port = 2345
s.bind(('', port))
s.listen(5)
while True:
    print('Server program started')
    c, addr = s.accept()
    mes = 'Thanks for connecting'
    mes = str.encode(mes)
    c.send(mes)
    c.close()
