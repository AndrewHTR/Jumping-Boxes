import pygame, sys, random
from pygame.locals import *
# Iniciador
pygame.init()

# Window
WINDOWWIDTH = 600
WINDOWHEIGHT = 400
screen = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption("Jumping Boxes")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)

clock = pygame.time.Clock()

# Cores
WHITE = (225, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (128,0,128)

# Boxes
UPLEFT = 'upleft'
UPRIGHT = 'upright'
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'

# Aleatoriedade de direção inicial:
DIRECAO = [UPLEFT, UPRIGHT, DOWNRIGHT, DOWNLEFT]

MOVESPEED = 4

caixa1 = {'rect':pygame.Rect(screen.get_width()//random.randrange(2,5), screen.get_height()//random.randrange(2,5),random.randrange(40,80), random.randrange(20,100)), 'color':PURPLE, 'dir':random.choice(DIRECAO)}
caixa2 = {'rect':pygame.Rect(screen.get_width()//random.randrange(2,5), screen.get_height()//random.randrange(2,5),random.randrange(40,80), random.randrange(20,100)), 'color':RED, 'dir':random.choice(DIRECAO)}
caixa3 = {'rect':pygame.Rect(screen.get_width()//random.randrange(2,5), screen.get_height()//random.randrange(2,5),random.randrange(40,80), random.randrange(20,100)), 'color':GREEN, 'dir':random.choice(DIRECAO)}
caixa4 = {'rect':pygame.Rect(screen.get_width()//random.randrange(2,5), screen.get_height()//random.randrange(2,5),random.randrange(40,80), random.randrange(20,100)), 'color':BLUE, 'dir':random.choice(DIRECAO)}

caixas = [caixa1, caixa2 , caixa3, caixa4]

# Looping para manter a tela aberta:
while True:
    # Adicionando a cor preta em toda a Surface:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # For usado como evento para caso a ação contida nele seja acionada        
    for caixa in caixas:
        # Direção inicial:
        if caixa['dir'] == DOWNRIGHT:
            caixa['rect'].left += MOVESPEED
            caixa['rect'].top += MOVESPEED

        if caixa['dir'] == DOWNLEFT:
            caixa['rect'].left -= MOVESPEED
            caixa['rect'].top += MOVESPEED

        if caixa['dir'] == UPRIGHT:
            caixa['rect'].left += MOVESPEED
            caixa['rect'].top -= MOVESPEED

        if caixa['dir'] == UPLEFT:
            caixa['rect'].left -= MOVESPEED
            caixa['rect'].top -= MOVESPEED

        # Colisão dos quadrados na tela:
        if caixa['rect'].top <= 0:
            if caixa['dir'] == UPLEFT:
                caixa['dir'] = DOWNLEFT
            if caixa['dir'] == UPRIGHT:
                caixa['dir'] = DOWNRIGHT

        if caixa['rect'].bottom >= WINDOWHEIGHT:
            if caixa['dir'] == DOWNLEFT:
                caixa['dir'] = UPLEFT
            if caixa ['dir'] == DOWNRIGHT:
                caixa['dir'] = UPRIGHT

        if caixa['rect'].left < 0:
            if caixa['dir'] == DOWNLEFT:
                caixa['dir'] = DOWNRIGHT
            if caixa['dir'] == UPLEFT:
                caixa['dir'] = UPRIGHT

        if caixa['rect'].right >= WINDOWWIDTH:
            if caixa['dir'] == DOWNRIGHT:
                caixa['dir'] = DOWNLEFT
            if caixa['dir'] == UPRIGHT:
                caixa['dir'] = UPLEFT


        # Desenhando todos os quadrados que estiverem na lista
        pygame.draw.rect(screen ,caixa['color'], caixa['rect']) 
    pygame.display.update()
    clock.tick(50)