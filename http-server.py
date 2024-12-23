import socket

# define socker host and port
SERVER_HOST = '0.0.0.0'
SERVER_PORT = 8000

# create socket variable
# set it to AF_INET (IPv4 address family)
# and SOCK_STREAM (TCP, basically)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(1)

print(f"listening on port {SERVER_PORT}")

while True:
    # wait for client connection
    client_connection, client_address = server_socket.accept()

    # get the client request
    request = client_connection.recv(1024).decode()
    print(request)

    # get index file
    with open('index.html', 'r') as file:
        content = file.read()

    # send http response
    response = "HTTP/1.0 200 OK\n\n" + content
    client_connection.sendall(response.encode())
    client_connection.close()

# close socket
server_socket.close()
