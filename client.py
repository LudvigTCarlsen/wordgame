import socket
from threading import Thread
from appJar import gui
import time

HOST = '127.0.0.1'
PORT = 12345
guess = ''
output = 'Enter playername and connect'
players = ['Connected:']



def btncallback(btn):

    if btn == 'submit':
        guess = app.getEntry('input')
        s.sendall(guess.encode('UTF-8'))
        app.clearEntry('input')

    if btn == 'connect':
        global output
        playername = '#%&' + app.getEntry('input')
        s.sendall(playername.encode('utf-8'))
        output = ''
        app.addButtons(['submit', 'quit'], btncallback)
        app.removeButton('connect')
        app.clearEntry('input')
        app.showLabel('players')

    if btn == 'quit':
        s.sendall('quitting'.encode('utf-8'))
        app.stop()
        
app = gui('Wordgame')
app.setSize('400x300')
app.setBg('salmon')
app.addLabel('players', players)
app.hideLabel('players')
app.addEntry('input')
app.setEntryMaxLength('input', 5)
app.addLabel('output', '')
app.addButton('connect', btncallback)


def receiving(s):
    while True:
        global output
        global players
        data = s.recv(256).decode('utf-8')
        if not data:
            break
        # #&% is char used to find usernames 
        if '#%&' in data:
            if data.strip('#%&') not in players:
                players.append(data.strip('#%&'))
                app.setLabel('players', players)
        elif 'sss' in data:
            output = f'Vinnaren är:  {data[3:len(data)]} \n ett nytt ord går att gissa på'
            app.setLabel('output', output)
        else:
            app.setLabel('output', data)

def main():
    global s
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST,PORT))
        Thread(target=receiving, args=(s,)).start()
        app.go()
        

if __name__ == "__main__":
    main()
    