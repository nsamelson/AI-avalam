import cherrypy
from cherrypy.lib.static import serve_file
import os
import sys
import webbrowser
import threading
import time
import socket
import json
from client import addClient, loadClients, clearClients, clientsList, removeClient
from transmitJSON import sendJSON, recvJSON

def getRootDir():
    return os.path.dirname(os.path.abspath(sys.argv[0]))

def manageClient(client, addr):
    data = recvJSON(client)
    data['ip']=addr[0]
    try:
        addClient(data)
        sendJSON(client, {'ok': True})
    except ValueError as e:
        sendJSON(client, {'ok': False, 'error': str(e)})
    finally:
        client.close()

def subscribeHandler():
    s = socket.socket()
    s.settimeout(0.5)
    s.bind(('0.0.0.0', 3001))
    s.listen()
    print('listen for subscription on port', 3001)
    while running:
        try:
            client, addr = s.accept()
            manageClient(client, addr)
        except socket.timeout:
            pass
    print('no more listen for subscription')

def startBrowser():
    time.sleep(2)
    webbrowser.open('http://localhost:3000')
    print('browser started !')

class Server:
    @cherrypy.expose(['game.js'])
    def game(self):
        cherrypy.response.headers['Content-Type'] = 'application/javascript'
        return gameJS

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def clients(self):
        return clientsList()

    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    def remove(self):
        data = cherrypy.request.json
        removeClient(data['name'])


if __name__ == '__main__':
    if len(sys.argv) > 1:
        game = sys.argv[1]
    else:
        game = 'matches'

    with open(os.path.join(getRootDir(),f'public/games/{game}.js')) as file:
        gameJS = file.read().encode('utf8')

    running = True
    threading.Thread(target=startBrowser).start()
    thread = threading.Thread(target=subscribeHandler)
    thread.start()

    def stop():
        print('STOPPING subscription handler...')
        global running
        running = False
        thread.join()
        print('subscription handler stopped')

    loadClients()
    cherrypy.engine.subscribe('stop', stop)
    cherrypy.quickstart(Server(), '', 'server.conf')
    