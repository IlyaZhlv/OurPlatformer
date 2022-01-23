import os
import sys

import pygame
player = None
WIDTH = 1920
HEIGHT = 1080
STEP = 8
FPS = 50
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

STARTTEXT = pygame.USEREVENT + 1
pygame.time.set_timer(STARTTEXT, 1000)

floor_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()
vrag_group = pygame.sprite.Group()
wall_group = pygame.sprite.Group()

pause_menu = {'restart': [147, 360, 196, 82], 'menu': [374, 360, 196, 82]}
def terminate():
    pygame.quit()
    sys.exit()

def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    if colorkey is not None:
        image = image.convert()
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image

def start_screen():
    scr = 0
    fon = load_image('fon.png')
    text = load_image('text.png')
    screen.blit(text, (0, 0))
    run = True
    while run:
        screen.fill(0)
        screen.blit(fon, (0, 0))
        if scr == 1:
            screen.blit(text, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN:
                run = False
            if event.type == STARTTEXT:
                scr = abs(scr - 1)
        pygame.display.flip()

def pause():
    screen.fill(pygame.Color(0, 0, 0))
    all_sprites.draw(screen)
    vrag_group.draw(screen)
    player_group.draw(screen)
    screen.blit(menu_images['pause_button'], (0, 0))
    screen.blit(menu_images['pause_menu'], (0, 0))
    if pygame.sprite.spritecollideany(player, vrag_group) != None:
        screen.fill(pygame.Color(0, 0, 0))
        tiles_group.draw(screen)
        vrag_group.draw(screen)
        screen.blit(menu_images['pause_button'], (0, 0))
        screen.blit(menu_images['pause_menu'], (0, 0))
        screen.blit(menu_images['dead'], (0, 0))
    pygame.display.flip()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminate()
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed(num_buttons=3)[0]:
                pos = pygame.mouse.get_pos()
                for i in pause_menu:
                    if pause_menu[i][0] < pos[0] < pause_menu[i][0] + pause_menu[i][2] and pause_menu[i][1] < pos[1] < pause_menu[i][1] + pause_menu[i][3]:
                        if i == 'restart':
                            return 'res'
                        elif i == 'menu':
                            return 'men'
                else:
                    return 'go'


tile_images = {'wall': load_image('wall.png'), 'empty': load_image('floor.png'),
               'yellow': load_image('yellow.png'), 'blue': load_image('blue.png'),
               'paint': load_image('painted_floor.png')}
menu_images = {'pause_button': load_image('pause.png'), 'pause_menu': load_image('pause_menu.png'),
               'dead': load_image('dead.png'), 'win': load_image('win.png')}
player_image = load_image('player.png')

tile_width = tile_height = 64

all_sprites = pygame.sprite.Group()
pause()
