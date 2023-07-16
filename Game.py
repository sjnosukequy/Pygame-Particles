from typing import Iterable, Union
import pygame
import sys, time

import Maps
from Settings import *

import Particles
import math
from itertools import cycle

class Game:
    def __init__(self):
        # self.Visible_sprite = Camera()
        # self.Obstacle_sprite = pygame.sprite.Group()
        # self.player = Player( (screen_w/2, screen_h/2), self.Obstacle_sprite, [self.Visible_sprite] )
        self.Map = Maps.Map()
        self.Particles = []

    def Run(self):
        self.Angle()
        mouse = pygame.mouse.get_pressed()
        if mouse[0]: #LEFT CLICK
            if Element == 0:
                MLOCO = pygame.mouse.get_pos()
                T = int(MLOCO[0] / size)
                L = int(MLOCO[1] / size)
                strloco = str(T) + ';' + str(L)
                if strloco not in Tiles_Map:
                    Tiles_Map[strloco] = [T, L , Color]

            if Element == -1:
                MLOCO = pygame.mouse.get_pos()
                T = int(MLOCO[0] / size)
                L = int(MLOCO[1] / size)
                strloco = str(T) + ';' + str(L)
                if strloco in Tiles_Map:
                    Tiles_Map.pop(strloco)

            if Element == 1:
                self.Particles.append(Particles.Smoke( pygame.mouse.get_pos(), Angle, Angle_bool ))
            if Element == 2:
                self.Particles.append(Particles.Fire( pygame.mouse.get_pos(), Angle, Angle_bool))
            if Element == 3:
                self.Particles.append(Particles.Water( pygame.mouse.get_pos(), Angle, Angle_bool))
            if Element == 4:
                self.Particles.append(Particles.Leaf( pygame.mouse.get_pos(), Angle, Angle_bool ))

        Maps.Draw_Grid(size)
        self.Map.Draw(size)
        # self.Visible_sprite.Custom_Draw(self.player, self.Particles)

        # pygame.draw.circle(screen, "BLACK", (screen_w/2,screen_h/2), 20)
        for i in self.Particles:
            if i.Kill == True and len(i.Particles) == 0:
                self.Particles.remove(i)
            i.Draw(size)

        Debug(Color)

    def Angle(self):
        global Angle
        mouse = pygame.mouse.get_pos()
        dx = mouse[0] - screen_w/2
        dy = mouse[1] - screen_h/2
        rads = math.atan2(-dy,dx)
        rads %= 2 * math.pi
        Angle = math.degrees(rads)


class Camera(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.Half_width = self.screen.get_size()[0] // 2
        self.Half_Height = self.screen.get_size()[1] // 2
        self.offset = pygame.math.Vector2()

        #CAMERA BOX
        self.Camera_Border = {'left': 100, 'right' : 100, 'top' : 100, 'bottom': 100}
        l = self.Camera_Border['left']
        t = self.Camera_Border['top']
        w = screen_w - (self.Camera_Border['left'] + self.Camera_Border['right'])
        h = screen_h - (self.Camera_Border['top'] + self.Camera_Border['bottom']) 
        self.Camera_rect = pygame.Rect(l,t,w,h)
        self.Loco = []

    def Box_Camera2(self, player):
            
            if player.hitbox.left < self.Camera_rect.left and player.Dir.x < 0:
                self.offset.x = player.hitbox.left - self.Camera_rect.left
                player.hitbox.left -= self.offset.x
                player.rect.center = player.hitbox.center
            elif player.rect.right > self.Camera_rect.right and player.Dir.x > 0:
                self.offset.x = player.hitbox.right - self.Camera_rect.right
                player.hitbox.right -= self.offset.x
                player.rect.center = player.hitbox.center
            else:
                self.offset.x = 0

            if player.rect.top < self.Camera_rect.top and player.Dir.y < 0:
                self.offset.y = player.hitbox.top - self.Camera_rect.top
                player.hitbox.top -= self.offset.y
                player.rect.center = player.hitbox.center
            elif player.rect.bottom > self.Camera_rect.bottom and player.Dir.y > 0:
                self.offset.y = player.hitbox.bottom - self.Camera_rect.bottom
                player.hitbox.bottom -= self.offset.y
                player.rect.center = player.hitbox.center
            else:
                self.offset.y = 0  

    def Custom_Draw(self, player, particles):
        global Tiles_Map
        #CALCULATING OFFSET
        self.Box_Camera2(player) 
        if self.offset.magnitude() != 0:
                for sprite in Tiles_Map:
                    if player.Dir.x > 0:
                        L = int(Tiles_Map[sprite][0] -1 )
                        T = int(Tiles_Map[sprite][1])
                    if player.Dir.x < 0:
                        L = int(Tiles_Map[sprite][0] + 1 )
                        T = int(Tiles_Map[sprite][1])
                    if player.Dir.y > 0:
                        T = int(Tiles_Map[sprite][1] - 1)
                        L = int(Tiles_Map[sprite][0])
                    if player.Dir.y < 0:
                        T = int(Tiles_Map[sprite][1] + 1)
                        L = int(Tiles_Map[sprite][0])
                    NStr_loco = str(L) + ';' + str(T)
                    self.Loco.append(NStr_loco)
                    Tiles_Map[sprite][0] = L
                    Tiles_Map[sprite][1] = T
                Tiles_Map = dict(zip(self.Loco, list(Tiles_Map.values())))
                self.Loco.clear()
                
                

        for sprite in sorted( self.sprites(), key= lambda sprite: sprite.rect.centery ):
            if sprite.Name == "Player" :
                # sprite.updateCol(Tiles_Map)
                pass
            else:
                sprite.rect.topleft -= self.offset
            self.screen.blit(sprite.image, sprite.rect)
        
        for sprite in particles:
            # sprite.offsetx = self.offset.x
            # sprite.offsety = self.offset.y
            sprite.Draw()
        


if __name__ == '__main__':
    pygame.init()
    #SCREEN
    clock = pygame.time.Clock()
    

    #FPS
    FPS = 60  #FRAMERATE LIMITER
    FPS_Target = 60
    Dt = 0
    Prev_Time = time.time()
    game = Game()

    Angle = 0
    Angle_bool = False

    Element = 1

    Colors = ["gold", "lightcoral", "red", "lightslateblue",  "blue", "orange", "white", "grey", "mediumspringgreen","mediumseagreen", "lightcoral", "green", "purple", "yellow", "black"]
    Colors_itter = cycle(Colors)
    Color = "black"

    while True:
        #DISPLAYING FPS
        pygame.display.set_caption(str(round(clock.get_fps(), 2)))
        #CALCULATING DELTA TIME
        clock.tick(FPS)
        now = time.time()
        Dt = (now - Prev_Time) * FPS_Target
        Prev_Time = now

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    Element = 1
                if event.key == pygame.K_2:
                    Element = 2
                if event.key == pygame.K_3:
                    Element = 3
                if event.key == pygame.K_4:
                    Element = 4
                if event.key == pygame.K_BACKQUOTE:
                    if Element == 0:
                        Color = next(Colors_itter)
                    Element = 0
                if event.key == pygame.K_ESCAPE:
                    Element = -1
                if event.key == pygame.K_TAB:
                    if Angle_bool:
                        Angle_bool = False
                    else:
                        Angle_bool = True
                if event.key == pygame.K_q:
                    if size > 15:
                        size -= 5
                if event.key == pygame.K_e:
                    if size < 40:
                        size += 5


        screen.fill("white")
        game.Run()

        pygame.display.flip()
