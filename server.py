import socket
import sys

#creating socket

def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("socket creation error : "+str(msg))

#Bind socket to port
def socket_binding():
    try:
        global host
        global port
        global s

        print("Binding socket to port "+str(port))
        print("Server is listning...")
        #bind port to server
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print(str(msg)+" Trying... ")
        socket_binding()

#Accept socket connection throught port
def socket_accept():
    conn, address = s.accept()
    print("Connection is established! IP : " + str(address[0]) + "|" + str(address[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        #getting user input via keyboard
        cmd = input()
        #Close all connections if user type quit in console
        if cmd == "quit":
            conn.close()
            s.close()
            sys.exit()
        #if client issue word more than 0
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")

def main():
    socket_create()
    socket_binding()
    socket_accept()

main()