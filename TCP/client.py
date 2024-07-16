import socket


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("localhost", 12345))

    print("Welcome to the Number Guessing Game!")

    while True:
        guess = input("Enter your guess (1-100): ")
        client_socket.sendall(guess.encode("utf-8"))

        response = client_socket.recv(1024).decode("utf-8")
        print(response)

        if "Correct!" in response:
            break

    client_socket.close()


if __name__ == "__main__":
    start_client()
