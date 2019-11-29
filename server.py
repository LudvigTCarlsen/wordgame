import socket
from threading import Thread
import functions



HOST = '127.0.0.1'
PORT = 12345
clients = {}
random_word = ''
newgame = 1


def receiving(conn):
    global newgame
    global random_word
    while True:
        if newgame:
            random_word = functions.gen_random_ord()
            newgame = 0
            print(random_word)
        data = conn.recv(256).decode('utf-8')
        if not data:
            break
        if data == 'quitting':
            conn.close()
            break
        if '#%&' in data:
            name = str(data)
            clients[conn] = name   

            for conn in clients:
                for names in clients:
                    returnvalue = clients[names]
                    conn.sendall(returnvalue.encode('utf-8'))
                

        elif functions.check_correct(data, random_word):
            returnvalue = 'sss' + clients[conn].strip('#%&')
            newgame = 1
            for conn in clients:
                conn.sendall(returnvalue.encode('utf-8'))
            continue

        else:
            clues = functions.hints(data, random_word)
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
        conn, adress = s.accept()
        print(conn)
        Thread(target=receiving, args=(conn,)).start()
        
    s.close

if __name__ == "__main__":
    main()
