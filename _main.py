from abc import ABC, abstractmethod
import pygame
pygame.init()

class Screen:
    def __init__(self, title=None, w = 0, h = 0) -> None:
        self.title      = title
        self._width     = w
        self._height    = h
        self._refresh_color = (0,0,0)


        self.frame  = pygame.display.set_mode((self._width, self._height))
        self.clock  = pygame.time.Clock()

        pygame.display.set_caption(self.title)

        self.text       = None
        self.textRect   = None

    def get_width(self):
        return self._width
        
    def get_height(self):
        return self._height

    def check_quit_pressed(self):
        quit_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_pressed = True

        return quit_pressed

    def push_text(self):
        pass

    def fill(self):
        self.frame.fill(self._refresh_color)

    def update(self):
        pygame.display.update()

    def tick(self, spd = 0):
        self.clock.tick(spd)

'''class Cmplx:
    def __init__(self, r, j):
        self.r = r
        self.j = j
        
    def __mul__(self, other):
        return self.r*other.r + self.r*other.j + self.j*other.r + self.j*other.j
        # TODO: implement imaginary component calculation
        
        
a = Cmplx(1, 2)
b = Cmplx(3, 4)

print(a*b)

# (1,2)(3,4)
'''


class ABC_Mandlebrot(ABC):

    # z1 = z0*z0 + c
    # z2 = z1*z1 + c
    # ...
    # zn = zn-1*zn-1 + c
    @abstractmethod
    def init_z(self, r, j): pass

    @abstractmethod
    def init_c(self, r, j): pass

    @abstractmethod
    def init_iter_depth(self, depth): pass

    @abstractmethod
    def calculate_next(self): pass


class Mandlebrot(ABC_Mandlebrot):
    def __init__(self) -> None:
        pass


class Main:
    def __init__(self):
        self.font_size = 0
        self.screen = Screen(title="Mandlebrot fun", w = 1000, h = 1000)
        self.mandlebrot = Mandlebrot()

    def mainloop(self) -> None:
        while not self.screen.check_quit_pressed():            
            pass

main    = Main()
main.mainloop()
