import socket

#preparing connection
my_socket = socket.socket()
IP_ADDRESS = socket.gethostbyname(socket.gethostname())
PORT = 5050
my_socket.connect(IP_ADDRESS, PORT)

#Creating and sending message
msg = "Hello, World!"
encoded_msg = msg.encode()
my_socket.send(encoded_msg)

#Recieving and decoding the message
encoded_data = my_socket.recv(1024)
decoded_data = encoded_data.decode()
print(f"The server sent: {decoded_data}")


#Closing the socket
my_socket.close()


