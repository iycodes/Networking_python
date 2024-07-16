import socket
import random
import threading


def handle_client(client_socket, addr):
    number_to_guess = random.randint(1, 100)
    print(f"Number to guess generated for {addr}.")

    while True:
        data, _ = client_socket.recvfrom(1024)
        guess = int(data.decode("utf-8"))
        print(f"Received guess {guess} from {addr}")

        if guess < number_to_guess:
            response = "Higher!"
        elif guess > number_to_guess:
            response = "Lower!"
        else:
            response = "Correct! You guessed the number!"
            client_socket.sendto(response.encode("utf-8"), addr)
            break

        client_socket.sendto(response.encode("utf-8"), addr)


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("localhost", 12345))
    print("Server is listening on port 12345...")

    while True:
        data, addr = server_socket.recvfrom(1024)  # Wait for initial contact
        print(f"Connection from {addr} has been established.")
        threading.Thread(target=handle_client, args=(server_socket, addr)).start()


if __name__ == "__main__":
    start_server()
