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

import os
import zipfile

class FS:
    def getPK3Package(packageName):
        return zipfile.ZipFile(os.path.dirname(os.path.abspath(__file__)) + "/../../" + packageName + ".pk3")

    def getExecDir():
        return os.path.dirname(os.path.abspath(__file__)) + "/../.."

    def isDir(path):
        return os.path.isdir(path)

    def isFile(path):
        return os.path.isFile(path)