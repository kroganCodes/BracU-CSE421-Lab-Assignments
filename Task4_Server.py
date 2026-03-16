import socket
port = 5051
data = 16
format = "utf-8"
disconnect_message = "end"


host_address = socket.gethostbyname(socket.gethostname())

server_socket_addr = (host_address, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(server_socket_addr)
server.listen()
print("Server is listening")


while True:
    conn, adrr = server.accept()
    print("Connected to ", adrr)

    connected = True

    while connected :
        ini = conn.recv(data).decode(format)

        print("Length of the message is ", len(ini))
        
        if ini :
            length = int(ini)
            message = conn.recv(length).decode(format)

            print("Message received ", message)

            if message ==disconnect_message :
                connected =False
                print("Terminating connection with ", adrr)
                conn.send("Nice to meet you".encode(format))

            else :
                hours =int(message)
                
                if hours<= 40 :
                    salary =hours*200
                else :
                    salary= 8000+(hours-40)*300

                conn.send(f"Salary is {salary} Taka".encode(format))


    conn.close()    