import os
import sys

import pygame
pygame.init()
player = None
WIDTH = 1920
HEIGHT = 1080
STEP = 8
FPS = 50

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


STARTTEXT = pygame.USEREVENT + 1
pygame.time.set_timer(STARTTEXT, 1000)
# тут должны быть наши тайлы
sprite = pygame.sprite.GroupSingle()
pause_menu = {'restart': [570, 610, 300, 300], 'menu': [1110, 623, 300, 300]}
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
    print("я снова с вами")
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
                import main
                from level import Level
                level = Level(screen)
                run = False
                break
            if event.type == STARTTEXT:
                scr = abs(scr - 1)
        pygame.display.flip()

def pause():
    all_sprites.draw(screen)
    sprite.draw(screen)
    sprite.draw(screen)
    screen.blit(menu_images['pause_menu'], (0, 0))
    #ecли смерть открывае вот это
    # if ded == True:
        # screen.fill(pygame.Color(0, 0, 0))
        # sprite.draw(screen)
        # sprite.draw(screen)
        # screen.blit(menu_images['pause_button'], (0, 0))
        # screen.blit(menu_images['pause_menu'], (0, 0))
        # screen.blit(menu_images['dead'], (0, 0))
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

                            print('restart')
                        elif i == 'menu':
                            start_screen()
                            print('menu')
                            break
                    else:
                        #продолжаем игру
                        print('продолжаем')

menu_images = {'pause_button': load_image('pause.png'), 'pause_menu': load_image('pause_menu.png'),
               'dead': load_image('dead.png'), 'win': load_image('win.png')}
player_image = load_image('player.png')

tile_width = tile_height = 64

all_sprites = pygame.sprite.Group()
