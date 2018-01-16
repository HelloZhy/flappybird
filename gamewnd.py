import pygame
import numpy.random as random


class gamewnd:
    def __init__(self):
        self.wndsize = (400, 400)
        self.hwnd = pygame.display.set_mode(self.wndsize)
        # background white
        self._bg = (255, 255, 255)
        self.hwnd.fill(self._bg)

        try:
            self._birdimg = pygame.image.load("./resource/bird_ss.jpg")
            self._pipeimg = pygame.image.load("./resource/pipe.jpg")
        except pygame.error as e:
            print('error: failed to load image')

        self.birdpos = [0, self.wndsize[1] / 2]
        self._num_of_pipe = 2
        # set the gap 150 px
        self._passwidth = 150
        self._pipespeed = 5
        # set the list of a pair of pipe format = (x, y)
        rand_height = random.randint(self._passwidth, 400-self._passwidth)
        self.pipeposlist = [[200-self._pipeimg.get_size()[0], random.randint(self._passwidth, 400-self._passwidth)],
                            [400-self._pipeimg.get_size()[0], random.randint(self._passwidth, 400-self._passwidth)]]
        self.hwnd.blit(self._birdimg, self.birdpos)
        for x in self.pipeposlist:
            up_pipe = [x[0], x[1]-self._pipeimg.get_size()[1]]
            down_pipe = [x[0], x[1]+self._passwidth]
            self.hwnd.blit(self._pipeimg, up_pipe)
            self.hwnd.blit(self._pipeimg, down_pipe)

    def game_restart(self):
        self.hwnd.fill(self._bg)
        self.birdpos = [0, self.wndsize[1] / 2]
        rand_height = random.randint(self._passwidth, 400-self._passwidth)
        self.pipeposlist = [[200-self._pipeimg.get_size()[0], random.randint(self._passwidth, 400-self._passwidth)],
                            [400-self._pipeimg.get_size()[0], random.randint(self._passwidth, 400-self._passwidth)]]
        self.hwnd.blit(self._birdimg, self.birdpos)
        for x in self.pipeposlist:
            up_pipe = [x[0], x[1]-self._pipeimg.get_size()[1]]
            down_pipe = [x[0], x[1]+self._passwidth]
            self.hwnd.blit(self._pipeimg, up_pipe)
            self.hwnd.blit(self._pipeimg, down_pipe)



    def get_hwnd(self):
        return self.hwnd

    def get_wnd_size(self):
        return self.wndsize

    def get_img_size(self, obj=None):
        dic = {'bird': self._birdimg, 'pipe': self._pipeimg, None: None}
        try:
            res = dic[obj].get_size()
        except pygame.error as e:
            print('error: no obj:', obj)
            return None
        return res


    def get_pass_width(self):
        return self._passwidth

    def set_bird_pos(self, dx=None, dy=None):
        # wnd clear
        self.hwnd.fill(self._bg)
        if self.birdpos[1] > self.wndsize[1] - self._birdimg.get_size()[1]:
            self.birdpos[1] = self.wndsize[1] - self._birdimg.get_size()[1]
        elif self.birdpos[1] < 0:
            self.birdpos[1] = 0
        else:
            self.birdpos[0] += dx
            self.birdpos[1] += dy
        self.hwnd.blit(self._birdimg, self.birdpos)

    def get_bird_pos(self):
        return self.birdpos

    def pipe_move_left(self):
        for x in self.pipeposlist:
            x[0] -= self._pipespeed
            if x[0] < -self._pipeimg.get_size()[0]:
                self.del_pipe()
            up_pipe = [x[0], x[1]-self._pipeimg.get_size()[1]]
            down_pipe = [x[0], x[1]+self._passwidth]
            self.hwnd.blit(self._pipeimg, up_pipe)
            self.hwnd.blit(self._pipeimg, down_pipe)

    def del_pipe(self):
        for x in self.pipeposlist:
            if x[0] <= -self._pipeimg.get_size()[0]:
                self.pipeposlist.remove(x)
            else:
                pass
        self.new_pipe()

    def new_pipe(self):
        # init x at right
        self.pipeposlist.append([400-self._pipeimg.get_size()[0],
                                 random.randint(self._passwidth, 400-self._passwidth)])
        for x in self.pipeposlist:
            up_pipe = [x[0], x[1]-self._pipeimg.get_size()[1]]
            down_pipe = [x[0], x[1]+self._passwidth]
            self.hwnd.blit(self._pipeimg, up_pipe)
            self.hwnd.blit(self._pipeimg, down_pipe)

