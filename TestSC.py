import Client
import Server
import threading

clientThread = threading.Thread(target=Client.run, args=())
serverThread = threading.Thread(target=Server.run, args=())

clientThread.daemon = True
serverThread.daemon = True

clientThread.start()
serverThread.start()
