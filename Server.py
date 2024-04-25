import socket

HOST = '0.0.0.0'  # Listen on all available network interfaces
PORT = 12345  # Choose a suitable port number

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))

    server_socket.listen()

    print('Server listening on {HOST}{PORT}')
    while True:
        conn, addr = server_socket.accept()
        with conn:
            print('Connected by', addr)
            data = conn.recv(1024)
            if not data:
                break
            print('Received data', data.decode())