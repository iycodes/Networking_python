import socket


def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ("localhost", 12345)

    print("Welcome to the Number Guessing Game!")

    while True:
        guess = input("Enter your guess (1-100): ")
        client_socket.sendto(guess.encode("utf-8"), server_address)

        response, _ = client_socket.recvfrom(1024)
        print(response.decode("utf-8"))

        if "Correct!" in response.decode("utf-8"):
            break

    client_socket.close()


if __name__ == "__main__":
    start_client()
