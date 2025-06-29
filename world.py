import pygame
from player import *
import math
import os
import json

class World():
    RoomIndex = 0

    editor = None

    RoomList = [[[1,4,5]]]
    f = open("save.txt", "r+")
    if os.path.getsize("save.txt") == 0:
        f.write("[[[1,4,5]]]")
    else:
        RoomList = json.loads(f.read())
    f.close()
    GridSize = 50

    sine = 0

    visualOffsetX = 0
    visualOffsetY = 0

    placeTransparency = 120

    def transparent_surface(self, alpha, color=(0, 0, 0)):
        surf = pygame.Surface([450, 500], pygame.SRCALPHA)
        surf.fill((color[0], color[1], color[2], alpha))
        return surf

    def render(self, screen, screenTrans):



        for obj in World.RoomList[World.RoomIndex]:
            if obj[0] == 1:
                if not World.editor:
                    pygame.draw.rect(screen, (255,125,0), [obj[1]*World.GridSize + World.visualOffsetX*1.3,obj[2]*World.GridSize + World.visualOffsetY,World.GridSize,World.GridSize])
                else:
                    pygame.draw.rect(screen, (75,200,0), [obj[1]*World.GridSize,obj[2]*World.GridSize,World.GridSize,World.GridSize])
            if obj[0] == 2:
                pygame.draw.rect(screen, (0,125,255), [obj[1]*World.GridSize + World.visualOffsetX,obj[2]*World.GridSize + World.visualOffsetY,World.GridSize,World.GridSize])

        if self.editor:
            pygame.draw.rect(screenTrans, (0,125,255), [int(pygame.mouse.get_pos()[0]/World.GridSize)*World.GridSize,int(pygame.mouse.get_pos()[1]/World.GridSize)*World.GridSize,World.GridSize,World.GridSize])


        pygame.font.init()

        font = pygame.font.SysFont("Callibri", 50)

        room_text = font.render(str(World.RoomIndex), True, (0,0,0))

        screen.blit(room_text, (5,5))

    def update(self):
        for obj in World.RoomList[World.RoomIndex]:
            if obj[0] == 1:
                obj[1] = Player.X
                obj[2] = Player.Y

        if not self.editor:
            World.visualOffsetX=World.sine
        else:
            self.visualOffsetX=0
        #print(World.visualOffsetX)

    def wallCheck(self, X, Y):
        if [2,X,Y] in World.RoomList[World.RoomIndex] or Y < 0 or Y > 9:
            if not self.editor:
                return True
            else:
                return False
        else:
            return False

    def plrCheck(self, X, Y):
        if [1,X,Y] in World.RoomList[World.RoomIndex]:
            return True
        else:
            return False