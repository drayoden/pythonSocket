import socket
import select

HEADER = 5
IP = "localhost"
PORT = 3500

ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # allows reconnect
ss.bind((IP,PORT))
ss.listen()

slist = [ss]    # list of clients/sockets
clients = {}    # dict of clients -> socket & data


# receive...
def rx_m(cs):
    try:
        mh = cs.recv(HEADER)
        if not len(mh):
            return False
        mlen = int(mh.decode("utf-8").strip())
        return {"header": mh, "data": cs.recv(mlen)}

    except:
        return False

while True:
    rs, _, es = select.select(slist, [], slist) # read sockets, _, exception sockets

    for nots in rs:
        if nots == ss:
            cs, caddr = ss.accept()
            user = rx_m(cs)
            if user is False:
                continue
            slist.append(cs)
            clients[cs] = user

            print(f"New connection from {caddr[0]}:{caddr[1]} username:{user['data'].decode('utf-8')}")

        else:
            m = rx_m(nots)

            if m is False:
                print(f"Closed connection from {clients[nots]['data'].decode('utf-8')}")
                slist.remove(nots)
                del clients[nots]

            user = clients[nots]
            print(f"Received message from {user['data'].decode('utf-8')}: {m['data'].decode('utf-8')}")

            for cs in clients:
                if cs != nots:
                    cs.send(user['header'] + user['data'] + m['header'] + m['data'])

    for nots in es:
        slist.remove(nots)
        del clients[nots]
