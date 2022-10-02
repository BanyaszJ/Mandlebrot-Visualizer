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


class Main:
    def __init__(self):
        self.font_size = 0
        self.screen = Screen(title="Mandlebrot fun", w = 1000, h = 1000)

    def mainloop(self) -> None:
        while not self.screen.check_quit_pressed():            
            pass

main    = Main()
main.mainloop()
