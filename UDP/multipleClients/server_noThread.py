import socket
import random


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("localhost", 12345))
    print("Server is listening on port 12345...")

    clients = {}  # Dictionary to store clients and their respective numbers to guess

    while True:
        data, addr = server_socket.recvfrom(1024)
        guess = int(data.decode("utf-8"))
        print(f"Received guess {guess} from {addr}")

        if addr not in clients:
            # Start a new game for the client
            number_to_guess = random.randint(1, 100)
            clients[addr] = number_to_guess
            print(f"Number to guess generated for {addr}.")

        number_to_guess = clients[addr]

        if guess < number_to_guess:
            response = "Higher!"
        elif guess > number_to_guess:
            response = "Lower!"
        else:
            response = "Correct! You guessed the number!"
            del clients[addr]  # Remove client after guessing correctly
            server_socket.sendto(response.encode("utf-8"), addr)
            continue  # Skip the next send

        server_socket.sendto(response.encode("utf-8"), addr)


if __name__ == "__main__":
    start_server()
