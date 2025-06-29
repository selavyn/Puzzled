import time

import pygame
from player import *
from world import *
import sys

if "editor" in sys.argv:
    World.editor=True
else:
    World.editor=False


running = True
(width, height) = (450, 500)
screen = pygame.display.set_mode((width, height))
screenTrans = pygame.Surface((width, height))
screenTrans.set_alpha(120)
screenTrans.set_colorkey((0,0,0))

if World.editor:
    pygame.display.set_caption("Puzzled Level Editor")
else:
    pygame.display.set_caption("Puzzled (Room 0)")
pygame.display.set_caption("Puzzled (Room 0)")
Clock = pygame.time.Clock()



while running:

    #print(World.RoomList[0])

    keys = pygame.key.get_pressed()


    Clock.tick(60)

    dt = Clock.get_time() / 400


    World.update(World)

    screenTrans.fill((0,0,0))

    screen.fill((255,255,255))


    World.render(World, screen, screenTrans)

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
            """if pygame.key.name(event.key) == "e":
                World.editor = not World.editor
                Player.X,Player.Y = int(Player.X),int(Player.Y)"""
            if pygame.key.name(event.key) == "c" and World.editor:
                World.RoomList=[[[1,4,5]]]
                Player.X,Player.Y,World.RoomIndex=4,5,0

            if pygame.key.name(event.key) == "right" and World.editor:
                World.RoomIndex+=1
            if pygame.key.name(event.key) == "left" and World.editor and World.RoomIndex>0:
                World.RoomIndex-=1

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                if World.editor:
                    if [2,int(pygame.mouse.get_pos()[0]/World.GridSize),int(pygame.mouse.get_pos()[1]/World.GridSize)] not in World.RoomList[World.RoomIndex]:
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


    if World.editor:
        if keys[pygame.K_d]:
            Player.X+=dt*Player.moveSpeedEditor
        if keys[pygame.K_q]:
            Player.X-=dt*Player.moveSpeedEditor
        if keys[pygame.K_z]:
            Player.Y-=dt*Player.moveSpeedEditor
        if keys[pygame.K_s]:
            Player.Y+=dt*Player.moveSpeedEditor

    if Player.X>=9:
        World.RoomList.append([[1, 3, 0]])
        Player.X=0
        World.RoomIndex+=1
        if not World.editor:
            pygame.display.set_caption(f'Puzzled (Room {World.RoomIndex})')

    if Player.X<0 and World.RoomIndex != 0:
        Player.X=8
        World.RoomIndex-=1
        if not World.editor:
            pygame.display.set_caption(f'Puzzled (Room {World.RoomIndex})')
    elif Player.X<0 and World.RoomIndex == 0:
        Player.X+=1

    ticks = pygame.time.get_ticks()/5
    World.sine = math.sin(ticks/50)*5

    screen.blit(screenTrans, (0,0))

    pygame.display.flip()