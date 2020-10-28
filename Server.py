import struct
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverAddress = ("0.0.0.0", 57785)

protocol = 1

startPosX = 0
startPosY = 0

clients = {}

def addClient(address):
    token = address[0] + ":" + str(address[1])
    clients[token] = {"username": None, "x": None, "y": None}

def getClient(address):
    token = address[0] + ":" + str(address[1])
    return clients[token]

def removeClient(address):
    token = address[0] + ":" + str(address[1])
    del clients[token]

def isClient(address):
    token = address[0] + ":" + str(address[1])
    if token in clients:
        return True
    else:
        return False

def sendPacket(data, address):
    return sock.sendto(data, address)

def receivePacket():
    return sock.recvfrom(65535)

ids = {
    "Login": 0x00,
    "LoginResponse": 0x01,
    "Spawn": 0x02,
    "Move": 0x03
}

login = {
    "id": ids["Login"],
    "protocol": None,
    "username": None
}

loginResponse = {
    "id": ids["LoginResponse"],
    "auth": None
}

spawn = {
    "id": ids["Spawn"],
    "x": None,
    "y": None
}

move = {
    "id": ids["Move"],
    "x": None,
    "y": None
}

def readLogin(data):
    login["id"] = data[0]
    login["protocol"] = struct.unpack(">L", data[1:1 + 4])[0]
    usernameSize = struct.unpack(">H", data[5:5 + 2])[0]
    login["username"] = data[7:7 + usernameSize].decode()

def writeLogin():
    data = b""
    data += struct.pack(">B", login["id"])
    data += struct.pack(">L", login["protocol"])
    data += struct.pack(">H", len(login["username"]))
    data += login["username"].encode()
    return data

def readLoginResponse(data):
    loginResponse["id"] = data[0]
    loginResponse["auth"] = data[1]

def writeLoginResponse():
    data = b""
    data += struct.pack(">B", loginResponse["id"])
    data += struct.pack(">B", loginResponse["auth"])
    return data

def readSpawn(data):
    spawn["id"] = data[0]
    spawn["x"] = struct.unpack(">L", data[1:1 + 4])[0]
    spawn["y"] = struct.unpack(">L", data[5:5 + 4])[0]

def writeSpawn():
    data = b""
    data += struct.pack(">B", spawn["id"])
    data += struct.pack(">L", spawn["x"])
    data += struct.pack(">L", spawn["y"])
    return data

def readMove(data):
    move["id"] = data[0]
    move["x"] = struct.unpack(">L", data[1:1 + 4])[0]
    move["y"] = struct.unpack(">L", data[5:5 + 4])[0]

def writeMove():
    data = b""
    data += struct.pack(">B", move["id"])
    data += struct.pack(">L", move["x"])
    data += struct.pack(">L", move["y"])
    return data

def handler(data, address):
    id = data[0]
    if id == ids["Login"]:
        readLogin(data)
        if login["protocol"] != protocol:
            loginResponse["auth"] = 0
            sendPacket(writeLoginResponse(), address)
            return
        loginResponse["auth"] = 1
        spawn["x"] = startPosX
        spawn["y"] = startPosY
        sendPacket(writeLoginResponse(), address)
        sendPacket(writeSpawn(), address)
        addClient(address)
        getClient(address)["username"] = login["username"]
    elif isClient(address):
        if id == ids["Move"]:
            client = getClient(address)
            readMove(data)
            client["x"] = move["x"]
            client["y"] = move["y"]
            
def movePlayer(address, x, y):
    move["x"] = x
    move["y"] = y
    sendPacket(writeMove(), address)

def run():
    sock.bind(serverAddress)
    recv = receivePacket()
    while True:
        if recv != None:
            data, address = recv
            handler(data, address)
