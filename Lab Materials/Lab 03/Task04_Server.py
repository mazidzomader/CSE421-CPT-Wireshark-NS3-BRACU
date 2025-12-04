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

def salary_calculator(amount):
    if amount <= 0:
        return 0
    if amount <= 40:
        return amount*200
    else:
        return 8000 + (300*(amount-40))

result  = salary_calculator(int(message))

server_socket.send(f"Calculated Salary: Tk {result}".encode(format))  
print("Sent Successfully")          
server_socket.close()
    