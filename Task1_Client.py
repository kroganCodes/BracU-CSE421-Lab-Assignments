import socket
port = 5050
data = 16
format = "utf-8"
disconnect_message = "end"


host_name = socket.gethostname()
host_address = socket.gethostbyname(host_name)

server_socket_addr = (host_address, port)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(server_socket_addr)


def send_message(message): 
    message= message.encode(format)
    length =str(len(message)).encode(format)
    length+= b" " * (data - len(length))
    
    client.send(length)
    client.send(message)

    print(client.recv(2048).decode(format))

send_message(f"IP address of the client is  {host_address} and the device name is {host_name}")
send_message(disconnect_message)


