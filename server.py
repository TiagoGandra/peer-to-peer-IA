import socket
import threading


def handle_client(client_socket, client_address, peer_sockets):
    while True:
        data = client_socket.recv(1024).decode("utf-8")
        if not data:
            break
        print(f"Received data from {client_address}: {data}")

        # Encaminha a mensagem para o outro cliente conectado
        for peer_socket in peer_sockets:
            if peer_socket != client_socket:
                peer_socket.send(data.encode("utf-8"))

    client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 8000))
    server_socket.listen(5)
    print("Server started. Listening for connections...")

    peer_sockets = []  # Lista para armazenar os sockets dos clientes conectados

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to {client_address}")

        # Adiciona o novo cliente à lista de sockets
        peer_sockets.append(client_socket)

        # Inicia uma nova thread para lidar com o cliente conectado
        client_thread = threading.Thread(
            target=handle_client, args=(client_socket, client_address, peer_sockets)
        )
        client_thread.start()


start_server()