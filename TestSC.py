import Client
import Server
import threading

serverThread = threading.Thread(target=Server.run, args=())
clientThread = threading.Thread(target=Client.run, args=())

serverThread.daemon = True
clientThread.daemon = True

serverThread.start()
clientThread.start()
