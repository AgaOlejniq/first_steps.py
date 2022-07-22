from asyncio import events
import pygame
from pygame.sprite import Sprite
import sys



class Game:
    def __init__(self):

        self.screen = pygame.display.set_mode((1200, 700))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Rain")

        self.drops = pygame.sprite.Group()
        self.make_rain()

    def run(self):
        while True:
            pygame.init()
            self.check_events()
            self.update_rain()
            #print(len(self.drops))

            self.update_screen()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_ESCAPE:
            sys.exit()

    def make_drop(self, drop_num, row_num):
        drop = Rain(self)
        drop_width, drop_height = drop.rect.size
        drop.x = drop_width + 2* drop_width * drop_num
        drop.rect.x = drop.x
        drop.rect.y = drop_height * row_num * 2
        
        self.drops.add(drop)

    def make_rain(self):
        drop = Rain(self)
        drop_width, drop_height = drop.rect.size
        avalible_space_x = self.screen_rect.width - (2* drop_width)
        drops_x = avalible_space_x // (2*drop_width)

        avalible_space_y = self.screen_rect.height - 4* drop_height
        drops_y = avalible_space_y // drop_height

        for row_num in range(drops_y):
            for drop_num in range(drops_x):
                self.make_drop(drop_num, row_num)

    def update_rain(self):
        for drop in self.drops.sprites():
            drop.rect.y += 3
        self._remove_rain()
        if len(self.drops) <= 7:
            self.make_rain()

    def _remove_rain(self):
        for drop in self.drops.copy():
            if drop.rect.top >= self.screen_rect.bottom:
                self.drops.remove(drop)     
            
    def update_screen(self):
        self.screen.fill((120,120,120))
        self.drops.draw(self.screen)
        pygame.display.flip()
        
class Rain(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.image = pygame.image.load(r"python_crash_course\part_2\pygame_excercises\drop.png")
        self.rect = self.image.get_rect()

        #start each new drop
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #store positon 
        self.y = float(self.rect.y)


g1 = Game()
g1.run()
