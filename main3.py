import pygame

pygame.init()

scr = pygame.display.set_mode((300, 300))
scr.fill(pygame.Color('green'))

def draw():
    pygame.draw.rect(scr, pygame.Color('black'), [(10, 10), (20, 250)], 0)
    pygame.draw.rect(scr, pygame.Color('blue'), [(30, 60), (200, 50)], 0)

draw()

while pygame.event.wait().type != pygame.QUIT:
    pygame.display.flip()

pygame.quit()