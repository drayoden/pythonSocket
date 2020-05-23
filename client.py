import socket
import pickle

HEADER = 5
BUFFER = 128
PORT = 3500

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), PORT))

mfull = b''
mnew = True

while True:
    m = s.recv(BUFFER)
    if mnew:
        # print(f'new message length: {m[:HEADER]}')
        mlen = int(m[:HEADER])
        mnew = False

    mfull += m

    if len(mfull)-HEADER == mlen:
        # print(mfull[HEADER:])
        d = pickle.loads(mfull[HEADER:])    # un-pickle
        print(d)
        mnew = True
        mfull = b''
