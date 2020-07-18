"""
*
*  __  __ _____ ____   ____                 _             
* |  \/  |  ___|  _ \ / ___| __ _ _ __ ___ (_)_ __   __ _ 
* | |\/| | |_  | | | | |  _ / _` | '_ ` _ \| | '_ \ / _` |
* | |  | |  _| | |_| | |_| | (_| | | | | | | | | | | (_| |
* |_|  |_|_|   |____/ \____|\__,_|_| |_| |_|_|_| |_|\__, |
*                                                    |___/ 
*
* Licensed under the Apache License, Version 2.0 (the "License")
* you may not use this file except in compliance with the License.
* You may obtain a copy of the License at http://www.apache.org/licenses/LICENSE-2.0
"""

from .FS import FS
import json

class MapManager:
    def getMaps():
        map = []
        time = 1
        for maps in FS.getPK3Package("game").namelist():
            if maps.startswith("MAPS/"):
                if not FS.isDir(maps):
                    if time == 1:
                        time += 1
                    else:
                        file = FS.getPK3Package("game").open(maps)
                        data = file.read()
                        decodedData = str(data.decode("utf-8"))
                        jsonData = json.loads(decodedData)
                        map.append(jsonData)
        return map

    def getMapName(num):
        return MapManager.getMaps()[num]['INFO']['NAME']

    def getNextMap(num):
        return int(MapManager.getMaps()[num]['INFO']['NEXT']) - 1

    def isSecretMap(num):
        secret = MapManager.getMaps()[num]['INFO']['SECRET'].lower()
        if secret == "yes":
            return True
        else:
            return False

    def getMapWidth(num):
        return MapManager.getMaps()[num]['DIMENSIONS']['WIDTH']

    def getMapHeight(num):
        return MapManager.getMaps()[num]['DIMENSIONS']['HEIGHT']

    def getPlayerStartPosX(num):
        return MapManager.getMaps()[num]['PLAYER']['START_POS_X']

    def getPlayerStartPosY(num):
        return MapManager.getMaps()[num]['PLAYER']['START_POS_Y']

    def getPlayerStartDirX(num):
        return MapManager.getMaps()[num]['PLAYER']['START_DIR_X']

    def getPlayerStartDirY(num):
        return MapManager.getMaps()[num]['PLAYER']['START_DIR_Y']

    def getWallsMap(num):
        return MapManager.getMaps()[num]['WALLS']

    def getCeilsMap(num):
        return MapManager.getMaps()[num]['CEILS']

    def getFloorsMap(num):
        return MapManager.getMaps()[num]['FLOORS']
