import socket
import threading


def handle_server(server_socket):
    while True:
        data = server_socket.recv(1024).decode("utf-8")
        if not data:
            break
        print(f"Received data from server: {data}")

    server_socket.close()


def start_client():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect(("localhost", 8000))
    print("Connected to server.")

    server_thread = threading.Thread(target=handle_server, args=(server_socket,))
    server_thread.start()

    while True:
        message = input("Enter a message: ")
        server_socket.send(message.encode("utf-8"))

    server_thread.join()


start_client()
