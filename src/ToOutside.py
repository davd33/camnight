import socket


def log(m):
    print(m)


def handle_client(s):
    s.send(bytes("Message\r\n"))
    data = s.recv(1024)
    log(data.decode(encoding='UTF-8'))


# create an INET, STREAMing socket
PORT = 8090
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((socket.gethostname(), PORT))
server_socket.listen(5)  # max connections

log("Socket server created on '" + socket.gethostname() + ":" + str(PORT) + "'.")

while 1:
    # accept connections from outside
    (client_socket, address) = server_socket.accept()

    # do stuff
    handle_client(client_socket)
