import socket
import random


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(("localhost", 12345))
    server_socket.listen(1)
    print("Server is listening on port 12345...")

    conn, addr = server_socket.accept()
    print(f"Connection from {addr} has been established!")

    number_to_guess = random.randint(1, 100)
    print("Number to guess has been generated.")

    while True:
        guess = conn.recv(1024).decode("utf-8")
        if not guess:
            break

        guess = int(guess)
        if guess < number_to_guess:
            conn.sendall("Higher!".encode("utf-8"))
        elif guess > number_to_guess:
            conn.sendall("Lower!".encode("utf-8"))
        else:
            conn.sendall("Correct! You guessed the number!".encode("utf-8"))
            break

    conn.close()
    server_socket.close()


if __name__ == "__main__":
    start_server()
