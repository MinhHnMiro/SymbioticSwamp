import socket
import threading

HEADER = 64
PORT = 5056
SERVER = socket.gethostbyname(socket.gethostname())
SERVER = '0.0.0.0'
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = '!DISCONNECT!'

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    print(f'[NEW CONNECTION] {addr} conneced')
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            conn.send('Message recieved'.encode(FORMAT))
    conn.close()

def start():
    server.listen()
    print('[LISTENING] Server is listening on ' + SERVER)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print('\n[ACTIVE CONNECTIONS] ' + str(threading.active_count() - 1))

print('[STARTING] Server is starting...')
start()
