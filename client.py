import network, _thread

n = network.network.Client()
n.Connect((input("server ipv4: "), 9898))

def PrintRecv(connection: network.network.Client):
    while True:
        print(f"received {connection.Recv(2048)} from {connection.connected_to}")

_thread.start_new_thread(PrintRecv, (n, ))
while True:
    n.Send(input(">> "))