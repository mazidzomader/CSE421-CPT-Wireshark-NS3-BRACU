import socket

port = 5050

data_length = 16
format = "utf-8"
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # using IPv4, TCP protocol

device_name = socket.gethostname()
server_ip = socket.gethostbyname(device_name)
client_ip = socket.gethostbyname(device_name)

server_socket_addr = (server_ip, port)

client.connect(server_socket_addr)

def sending_message(msg):
    message = msg.encode(format)
    msg_length = len(message)
    msg_length_str = str(msg_length).encode(format)
    msg_length_str += b" "*(data_length-len(msg_length_str))

    client.send(msg_length_str)
    client.send(message)

    # sent_from_server = client.recv(128).decode(format)
    # print("Sent from server:", sent_from_server)

sending_message(f"{client_ip} {device_name}")
