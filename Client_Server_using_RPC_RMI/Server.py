import socket

def server_program():
    host = socket.gethostname()  # Get the server's hostname
    port = 5001  # The port to which the server will bind

    server_socket = socket.socket()  # Create the socket object
    server_socket.bind((host, port))  # Bind the socket to the address and port
    server_socket.listen(2)  # Start listening for incoming connections

    print("Server is listening for connections on port", port)
    
    conn, address = server_socket.accept()  # Accept a connection from the client
    print("Connection from: " + str(address))

    while True:
        # Receive data from the client (max size: 1024 bytes)
        data = conn.recv(1024).decode()

        # If no data is received, break out of the loop
        if not data:
            print("No data received. Closing connection.")
            break

        # Print the received data
        print("from connected user: " + str(data))

        # Take input for the server's response (use raw_input() in Python 2.7)
        data = raw_input(' -> ')

        # Send the response back to the client
        conn.send(data.encode())

    # Close the connection after the loop ends
    conn.close()
    print("Connection closed.")

if __name__ == '__main__':
    server_program()







#A python program to illustrate Caesar Cipher Technique
def encrypt(text,s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if (char.isupper()):
            result += chr((ord(char) + s-65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result

#check the above function
text = "ALLARECAPS"
s = 4
print ("Text  : " + text)
print ("Shift : " + str(s))
print ("Cipher: " + encrypt(text,s))