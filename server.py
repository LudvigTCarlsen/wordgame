import socket
from threading import Thread
import functions
HOST = '127.0.0.1'
PORT = 1234
clients = {}


def messaging(conn):
    pass

def receiving(conn):
    #listens for data send through by client
    while True:
        guess = conn.recv(1024).decode('utf-8')
        if not guess:
            break
        if '##' in guess:
            clients[conn] = guess
            for key in clients: 
                for x in clients:
                    returnvalue = '@@'+ clients[x]
                    key.sendall(returnvalue.encode('utf-8'))
            continue
        clues = functions.hints(guess)
        returnvalue = clues.encode('utf-8')
        for key in clients:
            key.sendall(returnvalue)
    del clients[key]
    s.close()


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print('Listening...')
    while True:
        #accepts client connections in main thread
        conn, adress = s.accept()
        print(conn)
        clients[conn] = adress
        Thread(target=receiving, args=(conn,)).start()
        #thread for handling guesses received
        #thread for handling messages between clients
        Thread(target=messaging, args=(conn,)).start()
    s.close

if __name__ == "__main__":
    main()
