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
 
server_socket, client_add = server.accept()


upcoming_message_length = server_socket.recv(data_length).decode(format)

if upcoming_message_length:
    message = server_socket.recv(int(upcoming_message_length)).decode(format)

def vowel_count(msg):
    vowel = "aeiouAEIOU"
    vowel_count = 0
    for i in range(len(msg)):
        if msg[i] in vowel:
            vowel_count += 1
    if vowel_count <= 0:
        return vowel_count, "Not enough vowels"  
    elif vowel_count <= 2:
        return vowel_count, "Enough vowels I guess"
    else:
        return vowel_count,"Too many vowels"

count, result  = vowel_count(message)

server_socket.send(f"Vowel Count: {count}, {result}".encode(format))  
print("Sent Successfully")          
server_socket.close()
    