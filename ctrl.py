import pygame
from py_game.flappybird.gamewnd import gamewnd


class ctrl:
    def __init__(self, hwnd=None):
        self.hwnd = hwnd
        self.ifexit = False
        self.fly_speed = 10*0.75
        self.gravity = 5*0.75
        self._isflying = False
        self._counter = 20
        self._down_buffer = 0
        self.gameovermark = False
        self.game_ready = False

    def run(self):
        while not self.ifexit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.ifexit = True
                    break
                elif event.type == pygame.KEYDOWN:
                    if event.dict['unicode'] == ' ':
                        if not self.gameovermark:
                            self._isflying = True
                        else:
                            self.gameovermark = False
                else:
                    pass

            if not self.gameovermark:
                # if is flying
                if self._isflying and self._counter > 0:
                    self.bird_fly()
                    self._counter -= 1
                else:
                    self._counter = 20
                    self.bird_drop()
                    self._isflying = False
                #update pipe location
                self.hwnd.pipe_move_left()
            else:
                if not self.game_ready:
                    self.hwnd.game_restart()
                    self.game_ready = True

            # rule checking
            # edge detected
            for x in self.hwnd.pipeposlist:
                Xb, Yb = self.hwnd.get_img_size(obj='bird')
                Xp, _ = self.hwnd.get_img_size(obj='pipe')
                # Y detected
                if not x[1] < self.hwnd.get_bird_pos()[1] < x[1]+self.hwnd.get_pass_width()-Yb:
                    # X detected
                    if x[0]-Xb < self.hwnd.get_bird_pos()[0] < x[0]+Xp:
                        self.gameovermark = True
                        self.game_ready = False

            # graph update
            pygame.time.delay(5)
            pygame.display.update()

    def bird_fly(self):
        self.hwnd.set_bird_pos(dx=0, dy=-self.fly_speed+self.gravity*(20-self._counter)/20)

    def bird_drop(self):
        if self._counter > 0 and self._isflying:
            self._down_buffer = 1
        else:
            if self._down_buffer <= 160:
                self.hwnd.set_bird_pos(dx=0, dy=self.gravity*(160-self._down_buffer)/160)
                self._down_buffer += 1
            else:
                self._down_buffer = 1

