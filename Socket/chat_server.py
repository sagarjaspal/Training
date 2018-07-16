from socket import *


def server_program():
    host = gethostname()
    port = 5000
    server_socket = socket()
    server_socket.bind((host, port))
    server_socket.listen(2)
    print('Server is now running')
    conn, addr = server_socket.accept()
    print('Connection from ' + str(addr))
    while True:
        data = conn.recv(1024).decode()
        if not data:
            break
        print('From connected user: ' + str(data))
        data = input('>>>')
        conn.send(data.encode())
    conn.close()


if __name__ == '__main__':
    server_program()
