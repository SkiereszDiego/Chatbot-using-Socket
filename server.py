# challenge is to handle multiple conections

from email.base64mime import header_length
import socket
 # give us operating system-level IO capabilities, allawing this code to run the same in different SO,
 # using select is going to be far more efficient and will scale much better,
 # mainly since it's going to work on your OS layer, rather than all the way through Python.
import select

# starting values
header_length = 10
IP = "127.0.0.1"
PORT =  1234

# setup our socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#  set the following to overcome the "Address already in use". This modifies the socket to allow us to reuse the address, to reconnect.
# setsockopt(The thing you wanna set, What you wanna set of that thing, Set the thing)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#  bind and listen
server_socket.bind((IP, PORT))

server_socket.listen()

# list of sockets for select to keep track of, like "client list", it could be empty but there is already one(server_socket)
sockets_list = [server_socket]

# clients dict, client socket will be the key and the user data the value
clients = {}

# debugging
print(f'Listening for connections on {IP}:{PORT}...')

# The server's main job is to receive messages, and then disperse them to the connected clients.
# Handles message receiving
def receive_message(client_socket):
    try:
        pass

    except:

        # Something went wrong like empty message or client exited abruptly.
        return False