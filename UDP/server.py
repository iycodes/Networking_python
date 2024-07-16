import socket
import random


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(("localhost", 12345))
    print("Server is listening on port 12345...")

    number_to_guess = random.randint(1, 100)
    print("Number to guess has been generated.")

    while True:
        data, addr = server_socket.recvfrom(1024)
        guess = int(data.decode("utf-8"))
        print(f"Received guess {guess} from {addr}")

        if guess < number_to_guess:
            response = "Higher!"
        elif guess > number_to_guess:
            response = "Lower!"
        else:
            response = "Correct! You guessed the number!"
            server_socket.sendto(response.encode("utf-8"), addr)
            break

        server_socket.sendto(response.encode("utf-8"), addr)

    server_socket.close()


if __name__ == "__main__":
    start_server()
