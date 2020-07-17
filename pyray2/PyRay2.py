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
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide' # Hide pygame support message
import pygame
import tkinter
import tkinter.messagebox
import math
from threading import Thread
from utils.Options import Options
from utils.TextureManager import TextureManager
from utils.FS import FS

class PyRay2(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.daemon = True
        self.start()

        try:
            FS.getPK3Package("game")
        except:
            window = tkinter.Tk()
            window.wm_withdraw()
            tkinter.messagebox.showerror(title="Error", message="Game package not found!", parent=window)
            return

        # Game info
        gameName = 'PyRay2 - A python raycasting engine - '
        gameVersion = 'v2.0'
        
        # Check for options config
        if Options.checkForOptionsFile():
            Options.checkForOptionsFile()
        pygame.init()

        # Screen Variables
        screenWidth: int = Options.getScreenWidth()
        screenHeight: int = Options.getScreenHeight()
        if Options.isFullscreenOnRun() == True:
            screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
            isFullScreen: bool = True
        else:
            screen = pygame.display.set_mode((screenWidth, screenHeight))
            isFullScreen: bool = True
        pygame.display.set_caption(gameName + gameVersion)

        # Texture Variables
        textureMap = TextureManager.getTextures()
        textureMode = True

        running = True # Is the game running?
        clock = pygame.time.Clock()

        # Map Data
        worldMap =  [
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1],
                    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
                    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1],
                    [1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
                    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
                    ]

        # Player Variables
        px = 13.0 # Player x starting position
        py = 13.0 # Player y starting position
        pdx = 1.0 # Player x directional vector
        pdy = 0.0 # Player y directional vector
        cpx = 0.0 # The x 2d raycast version of camera plain
        cpy = 0.5 # The y 2d raycast version of camera plain
        rotSpeed = 0.05
        moveSpeed = 0.1 * clock.get_fps()

        # Trigeometric tuples + variables for index
        TGM = (math.cos(rotSpeed), math.sin(rotSpeed))
        ITGM = (math.cos(-rotSpeed), math.sin(-rotSpeed))
        COS, SIN = (0,1)

        while running == True:
            # Events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            if textureMode == False:
                # Draws roof and floor
                screen.fill((25,25,25))
                pygame.draw.rect(screen, (50,50,50), (0, int(screenHeight/2), screenWidth, int(screenHeight/2)))
            else:
                # Draws roof and floor
                screen.blit(pygame.transform.scale(textureMap[2], (screenWidth, screenHeight)), (0, 0))
                pygame.draw.rect(screen, (50,50,50), (0, int(screenHeight/2), screenWidth, int(screenHeight/2)))

            x = 0
            while x < screenWidth:
                x += 1
                # Calculate ray position and direction
                cx = 2.0 * x / screenWidth - 1.0
                rpx = px
                rpy = py
                rdx = pdx + cpx * cx
                rdy = pdy + cpy * cx + .000000000000001 # avoiding ZDE
        
                # Which box of the map the player is in
                mapX = int(rpx)
                mapY = int(rpy)
        
                # Length of the ray from current position to next x or y-side
                sideDistX = None
                sideDistY = None
        
                # Length of the ray from 1 x or y-side to next x or y-side
                deltaDistX = math.sqrt(1.0 + (rdy * rdy) / (rdx * rdx))
                deltaDistY = math.sqrt(1.0 + (rdx * rdx) / (rdy * rdy))
                perpWallDist = None
        
                # What direction to step in x or y-direction (either +1 or -1)
                stepX = None
                stepY = None
        
                hit = 0 # Was there a wall hit?  
                side = None # Was a NS or a EW wall hit?
        
                # Calculate step and initial sideDist
                if rdx < 0:
                    stepX = -1
                    sideDistX = (rpx - mapX) * deltaDistX
                else:
                    stepX = 1
                    sideDistX = (mapX + 1.0 - rpx) * deltaDistX
            
                if rdy < 0:
                    stepY = -1
                    sideDistY = (rpy - mapY) * deltaDistY
                else:
                    stepY = 1
                    sideDistY = (mapY + 1.0 - rpy) * deltaDistY

                # Perform DDA
                while (hit == 0):
                    # Jump to next sqare, or in x-direction, or in y-direction
                    if sideDistX < sideDistY:
                        sideDistX += deltaDistX
                        mapX += stepX
                        side = 0
                    else:
                        sideDistY += deltaDistY
                        mapY += stepY
                        side = 1
                    # Check if ray has hit a wall
                    if worldMap[mapX][mapY] > 0:
                        hit = 1
                
                # Calculate distance projected on Camera direction (Euclidean distance will give fishey effect!)
                if side == 0:
                    prepWallDist = abs((mapX - rpx + (1.0 - stepX) / 2.0) / rdx)
                else:
                    prepWallDist = abs((mapY - rpy + (1.0 - stepY) / 2.0) / rdy)
            
                # Calculate height of the line to draw on the screen
                lineHeight = abs(int(screenHeight / (prepWallDist + .0000001)))
        
                # Calculate lowest and highest pixel to fill in currentstripe
                drawStart = -lineHeight / 2.0 + screenHeight / 2.0
                if drawStart < 0:
                    drawStart = 0
                drawEnd = lineHeight / 2.0 + screenHeight / 2.0
                if drawEnd >= screenHeight:
                    drawEnd = screenHeight - 1
            
                if textureMode == False:
                    # Wall colors 0 to 3
                    wallcolors = [ [], [150,0,0], [0,150,0], [0,0,150] ]
                    color = wallcolors[ worldMap[mapX][mapY] ]  

                    # Draws Shadow
                    if side == 1:
                        for i,v in enumerate(color):
                            color[i] = int(v / 1.2)                    

                    # Drawing the graphics                        
                    pygame.draw.line(screen, color, (int(x), int(drawStart)), (int(x), int(drawEnd)), 2)
                else:
                    textureNumber = worldMap[mapX][mapY]
                    textureWidth = TextureManager.getTextureWidth(textureMap, textureNumber)
                    textureHeight = TextureManager.getTextureHeight(textureMap, textureNumber)
                    #calculate value of wallX
                    wallX = None
                    if side == 0:
                        wallX = py + prepWallDist * rdy
                    else:
                        wallX = px + prepWallDist * rdx
                    wallX -= math.floor((wallX))
            
                    # X coordinate on the texture
                    textureX = int(wallX * float(textureWidth))
                    if side == 0 and rdx > 0:
                        textureX = textureWidth - textureX - 1
                    if side == 1 and rdy < 0:
                        textureX = textureWidth - textureX - 1
                
                    # How much increase the texture coordinmate per screen pixel
                    step = 1.0 * textureHeight / lineHeight
                    # Starting texture coordinate
                    texturePos = (drawStart - screenHeight / 2 + lineHeight / 2) * step
                
                    textureY = int(texturePos) & (textureHeight - 1)
                    texturePos += step
            
                    c = max(1, (255.0 - prepWallDist * 27.2) * (1 - side * .25))
                    yStart = max(0, drawStart)
                    yStop = min(screenHeight, drawEnd)
                    pixelsPerTexel = lineHeight / textureHeight
                    colStart = int((yStart - drawStart) / pixelsPerTexel + .5)
                    colHeight = int((yStop - yStart) / pixelsPerTexel + .5)
                    yStart = int(colStart * pixelsPerTexel + drawStart + .5)
                    yHeight = int(colHeight * pixelsPerTexel + .5)
                    column = textureMap[textureNumber].subsurface((textureX, colStart, 1, colHeight))
                    column = column.copy()
                    if side == 1:
                        c = (int(c) >> 1) & 8355711
                    column.fill((c, c, c), special_flags = pygame.BLEND_MULT)
                    column = pygame.transform.scale(column, (2, yHeight))
                    screen.blit(column, (x, yStart))

            # Player controls
            if pygame.key.get_pressed()[pygame.K_LEFT]:
                opdx = pdx
                pdx = pdx * ITGM[COS] - pdy * ITGM[SIN]
                pdy = opdx * ITGM[SIN] + pdy * ITGM[COS]
                ocpx = cpx
                cpx = cpx * ITGM[COS] - cpy * ITGM[SIN]
                cpy = ocpx * ITGM[SIN] + cpy * ITGM[COS]

            if pygame.key.get_pressed()[pygame.K_RIGHT]:
                opdx = pdx
                pdx = pdx * TGM[COS] - pdy * TGM[SIN]
                pdy = opdx * TGM[SIN] + pdy * TGM[COS]
                ocpx = cpx
                cpx = cpx * TGM[COS] - cpy * TGM[SIN]
                cpy = ocpx * TGM[SIN] + cpy * TGM[COS]

            if pygame.key.get_pressed()[pygame.K_DOWN]:
                if not worldMap[int(px - pdx * moveSpeed)][int(py)]:
                    px -= pdx * moveSpeed
                if not worldMap[int(px)][int(py - pdy * moveSpeed)]:
                    py -= pdy * moveSpeed

            if pygame.key.get_pressed()[pygame.K_UP]:
                if not worldMap[int(px + pdx * moveSpeed)][int(py)]:
                    px += pdx * moveSpeed
                if not worldMap[int(px)][int(py + pdy * moveSpeed)]:
                    py += pdy * moveSpeed
            
            if pygame.key.get_pressed()[pygame.K_COMMA]:
                if not worldMap[int(px - cpx * moveSpeed)][int(py)]:
                    px -= cpx * moveSpeed
                if not worldMap[int(px)][int(py - cpy * moveSpeed)]:
                    py -= cpy * moveSpeed

            if pygame.key.get_pressed()[pygame.K_PERIOD]:
                if not worldMap[int(px + cpx * moveSpeed)][int(py)]:
                    px += cpx * moveSpeed
                if not worldMap[int(px)][int(py + cpy * moveSpeed)]:
                    py += cpy * moveSpeed

            if pygame.key.get_pressed()[pygame.K_LSHIFT]:
                rotSpeed = 0.1
                moveSpeed = 0.15
            if pygame.key.get_pressed()[pygame.K_RSHIFT]:
                rotSpeed = 0.1
                moveSpeed = 0.15
            else:
                rotSpeed = 0.05
                moveSpeed = 0.1
            
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
        
            if pygame.key.get_pressed()[pygame.K_F11]:
                if isFullScreen == False:
                    screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
                    isFullScreen = True
                else:
                    screen = pygame.display.set_mode((screenWidth, screenHeight))
                    isFullScreen = False

            # Updating display
            pygame.event.pump()
            pygame.display.flip()
            clock.tick(60)

PyRay2()
