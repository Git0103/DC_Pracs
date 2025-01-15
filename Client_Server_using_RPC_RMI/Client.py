import socket

def client_program():
    host = socket.gethostname()  # Get the hostname

    port = 5001  # Server port number

    client_socket = socket.socket()  # Create a socket object

    # Connect to the server
    client_socket.connect((host, port))

    message = raw_input(" -> ")  # Use raw_input() in Python 2.7

    while message.lower().strip() != 'bye':  # Continue until "bye" is sent
        # Send the input message to the server
        client_socket.send(message.encode())

        # Receive the server's response
        data = client_socket.recv(1024).decode()

        # Display the server's response
        print('Received from server: ' + data)

        # Take input for the next message
        message = raw_input(" -> ")  # Use raw_input() in Python 2.7

    client_socket.close()  # Close the connection

if __name__ == '__main__':
    client_program()
