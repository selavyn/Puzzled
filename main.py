import time

import pygame
from player import *
from world import *

running = True

(width, height) = (450, 500)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Puzzled")
Clock = pygame.time.Clock()


while running:

    #print(World.RoomList[0])
    Clock.tick(30)

    World.update(World)

    screen.fill((255,255,255))

    World.render(World, screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            f = open("save.txt", "r+")
            f.truncate(0)
            f.write(str(World.RoomList))
            f.close()
            running = False

        if event.type == pygame.KEYDOWN:
            if not World.editor:
                if pygame.key.name(event.key) == "d":
                    if not World.wallCheck(World, Player.X+Player.moveSquare, Player.Y):
                        Player.X+=Player.moveSquare
                if pygame.key.name(event.key) == "q":
                    if not World.wallCheck(World, Player.X-Player.moveSquare, Player.Y):
                        Player.X-=Player.moveSquare
                if pygame.key.name(event.key) == "z":
                    if not World.wallCheck(World, Player.X, Player.Y-Player.moveSquare):
                        Player.Y-=Player.moveSquare
                if pygame.key.name(event.key) == "s":
                    if not World.wallCheck(World, Player.X, Player.Y+Player.moveSquare):
                        Player.Y+=Player.moveSquare
            if pygame.key.name(event.key) == "e":
                World.editor = not World.editor

        if pygame.key.get_pressed():
            """if World.editor:
                if pygame.key.name() == "d":
                    Player.X+=Player.moveSpeedEditor
                if pygame.key.name(event.key) == "q":
                    Player.X-=Player.moveSpeedEditor
                if pygame.key.name(event.key) == "z":
                    Player.Y-=Player.moveSpeedEditor
                if pygame.key.name(event.key) == "s":
                    Player.Y+=Player.moveSpeedEditor"""

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if World.editor:
                    if [2,int(pygame.mouse.get_pos()[0]/World.GridSize),int(pygame.mouse.get_pos()[1]/World.GridSize)] not in World.RoomList[World.RoomIndex] and not World.plrCheck(World, int(pygame.mouse.get_pos()[0]/World.GridSize),int(pygame.mouse.get_pos()[1]/World.GridSize)):
                        World.RoomList[World.RoomIndex].insert(0,[2,int(pygame.mouse.get_pos()[0]/World.GridSize),int(pygame.mouse.get_pos()[1]/World.GridSize)])
                        print(World.RoomList)
                    else:
                        print("Non Accepted Spot")
            if event.button == 3:
                if World.editor:
                    if [2,int(pygame.mouse.get_pos()[0]/World.GridSize),int(pygame.mouse.get_pos()[1]/World.GridSize)] in World.RoomList[World.RoomIndex]:
                        World.RoomList[World.RoomIndex].remove([2,int(pygame.mouse.get_pos()[0]/World.GridSize),int(pygame.mouse.get_pos()[1]/World.GridSize)])
                        print(World.RoomList)
                    else:
                        print("Non Accepted Spot")

    if Player.X>=9:
        World.RoomList.append([[1, 3, 0]])
        Player.X=0
        World.RoomIndex+=1

    if Player.X<0 and World.RoomIndex != 0:
        Player.X=8
        World.RoomIndex-=1
    elif Player.X<0 and World.RoomIndex == 0:
        Player.X+=1

    ticks = pygame.time.get_ticks()/5
    World.sine = math.sin(ticks/50)*5

    pygame.display.update()