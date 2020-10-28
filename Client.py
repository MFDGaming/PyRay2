
import struct
import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

serverAddress = ("0.0.0.0", 57785)

protocol = 1

username = "PyRay2"

posX = 0
posY = 0

def sendPacket(data):
    return sock.sendto(data, serverAddress)

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
    
def loginToServer():
    login["protocol"] = protocol
    login["username"] = username
    sendPacket(writeLogin())
    while True:
        recv = receivePacket()
        if recv != None:
            data, address = recv
            id = data[0]
            print("Client: " + str(id))
            if id == ids["LoginResponse"]:
                readLoginResponse(data)
                if loginResponse["auth"] == 0:
                    break
            elif id == ids["Spawn"]:
                readSpawn(data)
                posX = spawn["x"]
                posY = spawn["y"]
                break

def handleMove():
    recv = receivePacket()
    data, address = recv
    id = data[0]
    if id == ids["Move"]:
        readMove(data)
        posX = move["x"]
        posY = move["y"]
            
def movePlayer(x, y):
    posX = x
    posY = y
    move["x"] = x
    move["y"] = y
    sendPacket(writeMove(), address)

def run():
    loginToServer()
    while True:
        handleMove()
