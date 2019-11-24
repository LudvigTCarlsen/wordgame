import socket
from threading import Thread
from appJar import gui
import time

HOST = '127.0.0.1'
PORT = 1234
guess = ''
data = 'Enter playername and connect'


def app(s):

    def update_output():
        while True:
            app.queueFunction(app.setLabel, "output", data)
            time.sleep(1)

    def btncallback(btn):

        if btn == 'submit':
            guess = app.getEntry('input')
            s.sendall(guess.encode('UTF-8'))
            app.clearEntry('input')
        if btn == 'connect':
            try:
                global data
                s.connect((HOST, PORT))
                playername = '###' + app.getEntry('input')
                s.sendall(playername.encode('utf-8'))
                data = ''

            except:
                data
                data = 'Failed to connect to server'
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
    app.addLabel('output', '')
    app.addButton('connect', btncallback)
    app.thread(update_output)
    app.go()
    

def receiving(s):
    while True:
        global data
        data = s.recv(1024).decode('utf-8')
        if not data:
            break
        
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
    