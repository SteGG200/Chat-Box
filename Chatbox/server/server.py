import socket
from _thread import *

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '192.168.1.12'
port = 8888

try :
    s.bind((server, port))
except socket.error as e :
    print(e)

s.listen()

print('Wait for connection')

names = []
clients = []

def connectedClient(conn):
    global clients,names
    name = conn.recv(2048).decode()
    names.append(name)
    while True :
        try :
            # print(names)
            data = conn.recv(2048).decode()
            # print(data)
            if not data : break
            # print(clients)
            for client in clients :
                client.send(str.encode(data))
        except Exception as e :
            print(e)
            break
    print('Disconnected')
    names.remove(name)
    clients.remove(conn)
    conn.close()



while True :
    conn,addr =  s.accept()

    print('Connected to',addr)
    clients.append(conn)
    start_new_thread(connectedClient,(conn,))