import socket
import select
import errno
import sys

HEADER = 5
IP = "localhost"
PORT = 3500

myuname = input("username: ")
cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cs.connect((IP,PORT))
cs.setblocking(False)

uname = myuname.encode("utf-8")
unameh = f"{len(uname):<{HEADER}}".encode("utf-8")
cs.send(unameh + uname)

while True:
    m = input(f"{myuname} > ")

    if m:
        m = m.encode("utf-8")
        mh = f"{len(m):<{HEADER}}".encode("utf-8")
        cs.send(mh + m)

    try:
        while True:
            unameh = cs.recv(HEADER)
            if not len(unameh):
                print("connection close by server...")
                sys.exit()

            unamel = int(unameh.decode("utf-8").strip())
            uname =  cs.recv(unamel).decode("utf-8")

            mh = cs.recv(HEADER)
            ml = int(mh.decode("utf-8"))
            m = cs.recv(ml).decode("utf-8")

            print(f"{uname} > {m}")

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error', str(e))
            sys.exit()
        continue

    except Exception as e:
        print("General error", str(e))
        sys.exit()
