import socket
from threading import Thread
from appJar import gui
import time

HOST = '127.0.0.1'
PORT = 1234
guess = ''
output = 'Enter playername and connect'
players = ['Connected:']


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
<<<<<<< Updated upstream
                playername = '##' + app.getEntry('input')
=======
                playername = '#%&' + app.getEntry('input')
>>>>>>> Stashed changes
                s.sendall(playername.encode('utf-8'))
                output = ''

            except:
                output = 'Failed to connect to server'
                s.close()

            Thread(target=receiving, args=(s,)).start()
            app.addButtons(['submit', 'cancel'], btncallback)
            app.removeButton('connect')
            app.clearEntry('input')
            app.showLabel('players')

        if btn == 'cancel':
            pass
    
    app = gui('Wordgame')
    app.setSize('400x300')
    app.setBg('salmon')
    app.addLabel('players', players)
    app.hideLabel('players')
    app.addEntry('input')
    app.setEntryMaxLength('input', 5)
    app.addLabel('output', '')
    app.addButton('connect', btncallback)
    app.thread(update_output)
    app.go()
    

def receiving(s):
    while True:
        global output
        data = s.recv(256).decode('utf-8')
        if not data:
            break
<<<<<<< Updated upstream
        # @@ are chars used to find usernames 
        if '@@' in data:
            if data[4:len(data)] in players:
                continue
            players.append(data[4:len(data)])
=======
        # ## is char used to find usernames 
        if '#%&' in data:
            if data.strip('#%&') not in players:
                players.append(data.strip('#%&'))
        elif 'sss' in data:
            output = 'Vinnaren är:' + data[3:len(data)]
>>>>>>> Stashed changes
        else:
            output = data
        
def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        Thread(target=app, args=(s,)).start()
        

if __name__ == "__main__":
    main()
    