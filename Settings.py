import pygame
screen_h = 720
screen_w = 720
size = 40
screen = pygame.display.set_mode( (screen_w, screen_h) )
Tiles_Map = { }


def Debug(attr):
    font = pygame.font.SysFont("Calibri", 20)
    text = str(attr)
    display = font.render(text, True, "white")
    rect = display.get_rect(topleft = (0 + 3, 0))
    pygame.draw.rect(screen, "black", rect)
    screen.blit(display, rect)