import pygame
from py_game.flappybird.gamewnd import gamewnd
from py_game.flappybird.ctrl import ctrl

core = None


# test ok, graph works well
def some_test():
    window = pygame.display.set_mode((200, 200))
    window.fill((255, 255, 255))
    print(type(window))
    try:
        bird = pygame.image.load('./resource/bird_s.jpg')
        window.blit(bird, (0, 0))
    except pygame.error as e:
        print('error: failed to load img')

    ifclosed = False

    while not ifclosed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ifclosed = True
                break
            elif event.type == pygame.KEYDOWN:
                if event.dict['unicode'] == ' ':
                    window.scroll(1, 0)
        pygame.display.update()


def game_init():
    # py_game package initialization
    global core
    pygame.init()
    core = ctrl(gamewnd())


def game_run():
    core.run()


def game_exit():
    # py_game package exit
    pygame.quit()


if __name__ == '__main__':
    game_init()
    game_run()
    game_exit()
