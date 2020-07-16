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
import pygame

class TextureManager:
    def loadTexture(texture):
        return pygame.image.load(FS.getPK3Package("game").open(texture)).convert()

    def getTextures():
        texture = [()]
        time = 1
        for textures in FS.getPK3Package("game").namelist():
            if textures.startswith("TEXTURES/"):
                if not FS.isDir(textures):
                    if time == 1:
                        time += 1
                    else:
                        texture.append((TextureManager.loadTexture(textures)))
        return texture

    def getTextureWidth(texture, num):
        return texture[num].get_size()[0]

    def getTextureHeight(texture, num):
        return texture[num].get_size()[1]