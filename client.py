import socket
from threading import Thread
from appJar import gui
import time

HOST = '127.0.0.1'
PORT = 1234
guess = ''
output = 'Enter playername and connect'
players = []


def app(s):

    def update_output():
        while True:
            app.queueFunction(app.setLabel, "output", output)
            app.queueFunction(app.setLabel, "players", players)

            time.sleep(1)

    def btncallback(btn):

        if btn == 'submit':
            guess = app.getEntry('input')
            s.sendall(guess.encode('UTF-8'))
            app.clearEntry('input')

        if btn == 'connect':
            try:
                global output
                s.connect((HOST, PORT))
                playername = '###' + app.getEntry('input')
                s.sendall(playername.encode('utf-8'))
                output = ''

            except:
                output = 'Failed to connect to server'
                s.close()

            Thread(target=receiving, args=(s,)).start()
            app.addButtons(['submit', 'cancel'], btncallback)
            app.removeButton('connect')
            app.clearEntry('input')

        if btn == 'cancel':
            pass
    
    app = gui('Wordgame')
    app.setSize('500x500')
    app.setBg('salmon')
    app.addEntry('input')
    app.addLabel('players', 'Players connected: ')
    app.addLabel('output', '')
    app.addButton('connect', btncallback)
    app.thread(update_output)
    app.go()
    

def receiving(s):
    while True:
        global output
        data = s.recv(1024).decode('utf-8')
        if not data:
            break
        # @@ is char used to find usernames 
        if '@@' in data:
            
            players.append(data[5:len(data)])
        else:
            output = data
        
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        Thread(target=app, args=(s,)).start()
        while True:
            try:
                s.sendall(guess.encode('UTF-8'))
            except:
                pass


if __name__ == "__main__":
    main()
    