import network, random, time, _thread


n = network.network.Server()
print(n.Create())
n.Start()

def PrintRecv(conn):
    while True:
        print(n.Recv(2048, conn))


while True:
    conn, addr = n.AcceptConn()
    n.Send("you are connected", conn)
    _thread.start_new_thread(PrintRecv, (conn, ))
    while True:
        r = str(random.randint(0, 42069))
        print(r)
        n.Send(r, conn)
        time.sleep(10)