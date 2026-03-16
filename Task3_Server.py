import socket
import threading


port = 5050
data = 16
format ="utf-8"
disconnect_message = "end"


host_address = socket.gethostbyname(socket.gethostname())

server_socket_addr = (host_address, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(server_socket_addr)
server.listen()
print("Server is listening")


def handler(conn, adrr) :
    
    print("Connected to ", adrr)

    connected = True

    while connected :
        ini = conn.recv(data).decode(format)

        print("Length of the message is ", len(ini))
        
        if ini :
            length = int(ini)
            message = conn.recv(length).decode(format)

            print("Message received ", message)

            if message == disconnect_message :
                connected = False
                print("Terminating connection with ", adrr)
                conn.send("Nice to meet you".encode(format))

            else :
                vow = "aeiouAEIOU"
                c = 0
                for i in message :
                    if i in vow :
                        c += 1
                if c == 0:
                    conn.send("Not enough vowels".encode(format))
                
                elif c <= 2:
                    conn.send("Enough vowels I guess".encode(format))

                else :
                    conn.send("Too many vowels".encode(format))




    conn.close()    

while True:
    conn, adrr = server.accept()
    thread = threading.Thread(target = handler, args = (conn, adrr))
    thread.start()