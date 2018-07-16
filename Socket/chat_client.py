from socket import *


def client_program():
    host = gethostname()
    port = 5000
    client_socket = socket()
    client_socket.connect((host, port))
    mes = input('>>>')
    while mes.lower().strip()!='bye':
        client_socket.send(mes.encode())
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print('From Server: ' + str(data))
        mes = input('>>>')
    client_socket.close()


if __name__ == '__main__':
    client_program()
