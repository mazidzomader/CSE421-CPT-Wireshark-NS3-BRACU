import socket

data_length = 16
port = 5050
format = "utf-8"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # using IPv4, TCP protocol

device_name = socket.gethostname()
server_ip = socket.gethostbyname(device_name)

server_socket_addr = (server_ip, port)

server.bind(server_socket_addr)

server.listen()
print("Server is listening...")
# while True: 
server_socket, client_add = server.accept()
# print("Connected to", client_add)

# connected = True
upcoming_message_length = server_socket.recv(data_length).decode(format)

if upcoming_message_length:
    message = server_socket.recv(int(upcoming_message_length)).decode(format)

    

    if message == "Disconnect":
        print("Disconnected with", client_add)
        connected = False

    cl_ip = message.split()[0]
    cl_device = message.split()[1]
    print(f"Client IP Address: {cl_ip} ||  Client Device Name: {cl_device}")
            
server_socket.close()
    