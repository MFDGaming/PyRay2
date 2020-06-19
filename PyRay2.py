"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
Author: MFDGaming
Repo: http://github.com/MFDGaming/PyRay2
""" 

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide' # Hide pygame support message
import pygame
import math
import time
import zipfile
import pygame
from pygame.locals import *

# Game info
gameName = 'PyRay2 - A python raycasting engine - '
gameVersion = 'v1.0'

pygame.init() # Initialize pygame

# Pygame screen
screenWidth = 1280
screenHeight = 960
screen = pygame.display.set_mode((screenWidth, screenHeight), pygame.FULLSCREEN)
pygame.display.set_caption(gameName + gameVersion)
isFullScreen = True

# Texture vars
textureMode = False
textureWidth = 256
textureHeight = 256

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
           
px = 13.0 # Player x starting position
py = 13.0 # Player y starting position
pdx = 1.0 # Player x directional vector
pdy = 0.0 # Player y directional vector
cpx = 0.0 # The x 2d raycast version of camera plain
cpy = 0.5 # The y 2d raycast version of camera plain
rotSpeed = 0.05
moveSpeed = 0.1


# Trigeometric tuples + variables for index
TGM = (math.cos(rotSpeed), math.sin(rotSpeed))
ITGM = (math.cos(-rotSpeed), math.sin(-rotSpeed))
COS, SIN = (0,1)

pygame.mixer.init()
pygame.mixer.music.load("./gb.mp3") 

running = True # Is the game running?
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    if pygame.mixer.music.get_busy() == False:
        pygame.mixer.music.play()
        
    # Draws roof and floor
    screen.fill((25,25,25))
    pygame.draw.rect(screen, (50,50,50), (0, int(screenHeight/2), screenWidth, int(screenHeight/2))) 
        
    column = 0
    while column < screenWidth:
        column += 1
        # Calculate ray position and direction
        cx = 2.0 * column / screenWidth - 1.0
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
            pygame.draw.line(screen, color, (int(column), int(drawStart)), (int(column), int(drawEnd)), 2)
        else:
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
            
            y = drawStart
            while y < drawEnd:
                y += 1
                textureY = int(texturePos) & (textureHeight - 1)
                texturePos += step

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

    if pygame.key.get_pressed()[K_LSHIFT]:
        rotSpeed = 0.1
        moveSpeed = 0.15
    elif pygame.key.get_pressed()[K_RSHIFT]:
        rotSpeed = 0.1
        moveSpeed = 0.15
    else:
        rotSpeed = 0.05
        moveSpeed = 0.1
            
    if pygame.key.get_pressed()[K_ESCAPE]:
        running = False
        
    if pygame.key.get_pressed()[K_F11]:
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
