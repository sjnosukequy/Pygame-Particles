import pygame
import random
from Settings import *

class Particles():
    def __init__(self, pos, angle, TTL, Color, angle_bool):
        super().__init__()
        self.pos = list(pos)
        self.angle = angle

        if angle_bool:
            if self.angle >= 0 and self.angle < 45:
                self.Vel = [random.randint(0, 10) / 10, random.randint(-10, 10) / 10]
            elif self.angle >= 45 and self.angle < 135:
                self.Vel = [random.randint(-10, 10) / 10, random.randint(-10, 0) / 10]
            elif self.angle >= 135 and self.angle < 225:
                self.Vel = [random.randint(-10, 0) / 10, random.randint(-10, 10) / 10]
            elif self.angle >= 225 and self.angle < 315:
                self.Vel = [random.randint(-10, 10) / 10, random.randint(0, 10) / 10]
            elif self.angle >= 315 and self.angle < 360:
                self.Vel = [random.randint(0, 10) / 10, random.randint(-10, 10) / 10]
        else:
            self.Vel = [random.randint(-10, 10) / 10, random.randint(-10, 10) / 10]

        self.TTL = TTL
        self.Color = Color
        self.offx = random.randint(-5, 5)
        self.offy = random.randint(-5, 5)
        # if Color == "grey":
        #     self.Color = random.choice( [(169,169,169), (190,190,190), (192,192,192) ] )
        # elif Color == "white":
        #     self.Color = random.choice( [(232,232,232), (240,240,240), (245,245,245) ] )

#FIX THE COLLSION FOLLOW THE CIRCLE
class Smoke():
    def __init__(self, pos, angle, Angle_bool):
        self.screen = pygame.display.get_surface()
        self.Speed = 2
        self.pos = pos
        self.angle = angle
        self.Particles = []

        self.Limit = 10
        self.count = 0
        self.offsetx = 0
        self.offsety = 0
        self.Kill = False
        self.Angle_bool = Angle_bool

    def Draw(self, size):
        # self.count = max(self.count, len(self.Particles) )
        if self.count <= self.Limit:
            if not self.Kill:
                # Color = random.choice( [(232,232,232), (240,240,240), (245,245,245), (169,169,169), (190,190,190), (192,192,192) ] )
                Color = "white"
                self.Particles.append( Particles( self.pos, self.angle, random.randint(15,20), Color, self.Angle_bool) )
                self.count += 1
        else:
            self.Kill = True 

        for i in self.Particles:
            self.Collision(i, "Hoz", size)
            self.Collision(i, "Ver", size)

            i.pos[0] -= self.offsetx
            i.pos[1] -= self.offsety
            
            i.pos[0] += i.Vel[0] * self.Speed
            i.pos[1] += i.Vel[1] * self.Speed
            i.TTL -= 0.1
            
            if i.TTL <= 14:
                i.Color = (190,190,190)
            if i.TTL <= 10:
                i.Color = (169,169,169)
            if i.TTL <= 3:
                i.Color = (109, 93, 110)

            pygame.draw.circle(self.screen, i.Color, i.pos, i.TTL)
            if i.TTL < 0:
                self.Particles.remove(i)

    def Collision(self, sprite, check, size):
        if check == "Hoz":
            str_loccTL = str(int(sprite.pos[0] / size)) + ';' + str(int(sprite.pos[1] / size))
            str_loccBR = str(int( (sprite.pos[0] + sprite.TTL + sprite.offx ) / size)) + ';' + str(int( (sprite.pos[1] + sprite.TTL + sprite.offy ) / size))
            if str_loccTL in Tiles_Map or str_loccBR in Tiles_Map :
                sprite.Vel[0] = -1 * sprite.Vel[0]
        else:
            str_loccTL = str(int(sprite.pos[0] / size)) + ';' + str(int(sprite.pos[1] / size))
            str_loccBR = str(int( (sprite.pos[0] + sprite.TTL + sprite.offx ) / size)) + ';' + str(int( (sprite.pos[1] + sprite.TTL + sprite.offy ) / size))
            if str_loccTL in Tiles_Map or str_loccBR in Tiles_Map :
                sprite.Vel[1] = -1 * sprite.Vel[1] 

class Fire():
    def __init__(self, pos, angle, Angle_bool):
        self.screen = pygame.display.get_surface()
        self.Speed = 2
        self.pos = pos
        self.angle = angle
        self.Particles = []

        self.Limit = 10
        self.count = 0
        self.offsetx = 0
        self.offsety = 0
        self.Kill = False
        self.Angle_bool = Angle_bool
    def Draw(self, size):
        # self.count = max(self.count, len(self.Particles) )
        if self.count <= self.Limit:
            if not self.Kill:
                # Color = random.choice( [(232,232,232), (240,240,240), (245,245,245), (169,169,169), (190,190,190), (192,192,192) ] )
                Color = "white"
                self.Particles.append( Particles( self.pos, self.angle, random.randint(15,20), Color, self.Angle_bool) )
                self.count += 1
        else:
            self.Kill = True 

        for i in self.Particles:
            self.Collision(i, "Hoz", size)
            self.Collision(i, "Ver", size)

            i.pos[0] -= self.offsetx
            i.pos[1] -= self.offsety
            
            i.pos[0] += i.Vel[0] * self.Speed
            i.pos[1] += i.Vel[1] * self.Speed
            i.TTL -= 0.1
            
            if i.TTL <= 14:
                i.Color = "yellow"
            if i.TTL <= 10:
                i.Color = "orange"
            if i.TTL <= 3:
                i.Color = "red"

            pygame.draw.circle(self.screen, i.Color, i.pos, i.TTL)
            if i.TTL < 0:
                self.Particles.remove(i)

    def Collision(self, sprite, check, size):
        if check == "Hoz":
            str_loccTL = str(int(sprite.pos[0] / size)) + ';' + str(int(sprite.pos[1] / size))
            str_loccBR = str(int( (sprite.pos[0] + sprite.TTL + sprite.offx ) / size)) + ';' + str(int( (sprite.pos[1] + sprite.TTL + sprite.offy ) / size))
            if str_loccTL in Tiles_Map or str_loccBR in Tiles_Map :
                sprite.Vel[0] = -1 * sprite.Vel[0]
        else:
            str_loccTL = str(int(sprite.pos[0] / size)) + ';' + str(int(sprite.pos[1] / size))
            str_loccBR = str(int( (sprite.pos[0] + sprite.TTL + sprite.offx ) / size)) + ';' + str(int( (sprite.pos[1] + sprite.TTL + sprite.offy ) / size))
            if str_loccTL in Tiles_Map or str_loccBR in Tiles_Map :
                sprite.Vel[1] = -1 * sprite.Vel[1] 
                
class Water():
    def __init__(self, pos, angle, Angle_bool):
        self.screen = pygame.display.get_surface()
        self.Speed = 2
        self.pos = pos
        self.angle = angle
        self.Particles = []

        self.Limit = 10
        self.count = 0
        self.offsetx = 0
        self.offsety = 0
        self.Kill = False
        self.Angle_bool = Angle_bool

    def Draw(self, size):
        # self.count = max(self.count, len(self.Particles) )
        if self.count <= self.Limit:
            if not self.Kill:
                # Color = random.choice( [(37, 53, 211), (51, 230, 253), (187, 224, 251), (255, 251, 255) ] )
                Color = (37, 53, 211)
                self.Particles.append( Particles( self.pos, self.angle, random.randint(18,20), Color, self.Angle_bool) )
                self.count += 1
        else:
            self.Kill = True 

        for i in self.Particles:
            self.Collision(i, "Hoz", size)
            self.Collision(i, "Ver", size)

            i.pos[0] -= self.offsetx
            i.pos[1] -= self.offsety
            
            i.pos[0] += i.Vel[0] * self.Speed
            i.pos[1] += i.Vel[1] * self.Speed
            i.TTL -= 0.1
            
            if i.TTL <= 17:
                i.Color = (24, 128, 255)
            if i.TTL <= 14:
                i.Color = (39, 168, 252)
            if i.TTL <= 10:
                i.Color = random.choice( [ (187, 224, 251), (255, 251, 255) ] )

            pygame.draw.circle(self.screen, i.Color, i.pos, i.TTL)
            if i.TTL < 0:
                self.Particles.remove(i)

    def Collision(self, sprite, check, size):
        if check == "Hoz":
            str_loccTL = str(int(sprite.pos[0] / size)) + ';' + str(int(sprite.pos[1] / size))
            str_loccBR = str(int( (sprite.pos[0] + sprite.TTL + sprite.offx ) / size)) + ';' + str(int( (sprite.pos[1] + sprite.TTL + sprite.offy ) / size))
            if str_loccTL in Tiles_Map or str_loccBR in Tiles_Map :
                sprite.Vel[0] = -1 * sprite.Vel[0]
        else:
            str_loccTL = str(int(sprite.pos[0] / size)) + ';' + str(int(sprite.pos[1] / size))
            str_loccBR = str(int( (sprite.pos[0] + sprite.TTL + sprite.offx ) / size)) + ';' + str(int( (sprite.pos[1] + sprite.TTL + sprite.offy ) / size))
            if str_loccTL in Tiles_Map or str_loccBR in Tiles_Map :
                sprite.Vel[1] = -1 * sprite.Vel[1] 

#THE COLLSION CORRECT FOR THE ELLIPSE       
class Leaf():
    def __init__(self, pos, angle, Angle_bool):
        self.screen = pygame.display.get_surface()
        self.Speed = 2
        self.pos = pos
        self.angle = angle
        self.Particles = []

        self.Limit = 10
        self.count = 0
        self.offsetx = 0
        self.offsety = 0
        self.Kill = False
        self.Angle_bool = Angle_bool
    def Draw(self, size):
        # self.count = max(self.count, len(self.Particles) )
        if self.count <= self.Limit:
            if not self.Kill:
                # Color = random.choice( [(37, 53, 211), (51, 230, 253), (187, 224, 251), (255, 251, 255) ] )
                Color = (19, 99, 56)
                self.Particles.append( Particles( self.pos, self.angle, random.randint(18,20), Color, self.Angle_bool) )
                self.count += 1
        else:
            self.Kill = True 

        for i in self.Particles:
            self.Collision(i, "Hoz", size)
            self.Collision(i, "Ver", size)

            i.pos[0] -= self.offsetx
            i.pos[1] -= self.offsety

            i.pos[0] += i.Vel[0] * self.Speed
            i.pos[1] += i.Vel[1] * self.Speed
            i.TTL -= 0.1
            
            if int(i.TTL) == 17:
                i.Color = random.choice( [(50, 130, 85), (19, 99, 56)])
            if int(i.TTL) == 14:
                if i.Color == (50, 130, 85):
                    i.Color = random.choice( [(50, 130, 85), (81, 157, 122)])
            if int(i.TTL) == 10:
                # if i.Color == (81, 157, 122):
                #     i.Color = random.choice( [ (81, 157, 122),(81, 157, 122),(81, 157, 122), (81, 157, 122), (115, 195, 152), (147, 236, 178) ] )
                if i.Color == (81, 157, 122):
                    i.Color = random.choice( [(115, 195, 152), (81, 157, 122)])
            

            pygame.draw.ellipse(self.screen, i.Color, (i.pos[0], i.pos[1], i.TTL + i.offx, i.TTL + i.offy))
            if i.TTL < 0:
                self.Particles.remove(i)

    def Collision(self, sprite, check, size):
        if check == "Hoz":
            str_loccTL = str(int(sprite.pos[0] / size)) + ';' + str(int(sprite.pos[1] / size))
            str_loccBR = str(int( (sprite.pos[0] + sprite.TTL + sprite.offx ) / size)) + ';' + str(int( (sprite.pos[1] + sprite.TTL + sprite.offy ) / size))
            if str_loccTL in Tiles_Map or str_loccBR in Tiles_Map :
                sprite.Vel[0] = -1 * sprite.Vel[0]
        else:
            str_loccTL = str(int(sprite.pos[0] / size)) + ';' + str(int(sprite.pos[1] / size))
            str_loccBR = str(int( (sprite.pos[0] + sprite.TTL + sprite.offx ) / size)) + ';' + str(int( (sprite.pos[1] + sprite.TTL + sprite.offy ) / size))
            if str_loccTL in Tiles_Map or str_loccBR in Tiles_Map :
                sprite.Vel[1] = -1 * sprite.Vel[1] 