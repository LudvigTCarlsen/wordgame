import socket
from threading import Thread
import functions
import sys



HOST = '127.0.0.1'
PORT = 1234
clients = {}
word = ''
newgame = 1


def messaging(conn):
    pass

def receiving(conn):
    #listens for data send through by client
    newgame = 1
    global word
    while True:
        data = conn.recv(256).decode('utf-8')
        if not data:
            break
        if '#%&' in data:
            if newgame:
                word = functions.gen_random_ord()
                print(word)
                newgame = 0
            clients[conn] = data
            for conn in clients:
                for values in clients:
                    returnvalue = clients[values]
                    conn.sendall(returnvalue.encode('utf-8'))
            continue

        if functions.check_correct(data, word):
            returnvalue = 'sss' + clients[conn].strip('#%&')
            for conn in clients:
                conn.sendall(returnvalue.encode('utf-8'))
            continue

        clues = functions.hints(data, word)
        returnvalue = clues.encode('utf-8')
        for conn in clients:
            conn.sendall(returnvalue)
    del clients[conn]
    conn.close()


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
