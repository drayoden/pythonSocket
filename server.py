import socket
import time
import pickle   # serialize data

HEADER = 5
PORT = 3500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), PORT))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} established...")

    d = {1:"Welcome", 2:"to", 3:"yoda!"}
    m = pickle.dumps(d)
    m = bytes(f'{len(m):<{HEADER}}', "utf-8") + m

    clientsocket.send(m)

    while True:
        time.sleep(2)
        d = {1:'Waiting', 2:'for', 3:'next', 4:'message'}
        m = pickle.dumps(d)
        m = bytes(f'{len(m):<{HEADER}}', "utf-8") + m
        try:
            clientsocket.send(m)
        except BrokenPipeError:
            print('Connection broken...')
            exit(1)
