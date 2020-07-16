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

import json
import os
from .FS import FS

optionTemplate = {
    "GFX": {
        "SCREEN_WIDTH": 640,
        "SCREEN_HEIGHT": 480
    },
    "DEBUG": "OFF",
    "FULLSCREEN_ONRUN": "ON"
}


class Options:
    @staticmethod
    def checkForOptionsFile() -> bool:
        file = os.path.isfile(FS.getExecDir() + '/options.json')
        if not file:
            with open(FS.getExecDir() + '/options.json', 'w+') as newFile:
                json.dump(optionTemplate, newFile, indent=4)
                newFile.close()
            return True
        else:
            return True

    @staticmethod
    def getScreenWidth() -> int:
        with open(FS.getExecDir() + '/options.json', 'r') as file:
            options = json.loads(file.read())
            screenWidth = options['GFX']['SCREEN_WIDTH']
            file.close()
            return int(screenWidth)

    @staticmethod
    def getScreenHeight() -> int:
        with open(FS.getExecDir() + '/options.json', 'r') as file:
            options = json.loads(file.read())
            screenHeight = options['GFX']['SCREEN_HEIGHT']
            file.close()
            return int(screenHeight)

    @staticmethod
    def isDebugMode() -> bool:
        with open(FS.getExecDir() + '/options.json', 'r') as file:
            options = json.loads(file.read())
            debug = options['DEBUG']
            file.close()
            if debug.lower() == "on":
                return True
            else:
                return False

    @staticmethod
    def isFullscreenOnRun() -> bool:
        with open(FS.getExecDir() + '/options.json', 'r') as file:
            options = json.loads(file.read())
            fullscreen = options['FULLSCREEN_ONRUN']
            file.close()
            if fullscreen.lower() == "on":
                return True
            else:
                return False