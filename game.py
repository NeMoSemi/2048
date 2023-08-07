import random

import pygame
from functions import load_image, get_random_number
from configfile import screen, game_size, size_of_map


class GameFon(pygame.sprite.Sprite):
    main_image = load_image("img\system\main.png")
    map_image = load_image("img\system\map.png")
    kletka_image = load_image("img\system\kletka.png")

    def __init__(self, *group):
        super().__init__(*group)
        self.main_image = GameFon.main_image
        self.main_image = pygame.transform.scale(self.main_image, game_size)

        self.kletka_image = GameFon.kletka_image
        self.kletka_image = pygame.transform.scale(self.kletka_image, (100, 100))

        self.map_image = GameFon.map_image
        self.map_size = size_of_map * 100 + 15 * (size_of_map + 1)
        self.map_image = pygame.transform.scale(self.map_image, (self.map_size, self.map_size))

        self.bottom = (game_size[0] - self.map_size) // 2

        self.map_x_pos = game_size[0] - self.map_size - self.bottom
        self.map_y_pos = game_size[1] - self.map_size - self.bottom
        self.map_pos = (self.map_x_pos, self.map_y_pos)

    def update(self, *args):
        screen.blit(self.main_image, (0, 0))
        screen.blit(self.map_image, self.map_pos)
        for x in range(1, size_of_map + 1):
            for y in range(1, size_of_map + 1):
                screen.blit(self.kletka_image, (self.bottom + 15 * x + 100 * (x - 1),
                                                self.map_y_pos + 15 * y + 100 * (y - 1)))

    def game_x_bottom(self):
        return self.bottom

    def game_y_bottom(self):
        return self.map_y_pos


class GameCycle(pygame.sprite.Sprite):
    digits = {2: 'img\digits\d2.png', 4: 'img\digits\d4.png', 8: 'img\digits\d8.png', 16: 'img\digits\d16.png',
              32: 'img\digits\d32.png', 64: 'img\digits\d64.png', 128: 'img\digits\d128.png',
              256: 'img\digits\d256.png', 512: 'img\digits\d512.png', 1024: 'img\digits\d1024.png',
              2048: 'img\digits\d2048.png', 4096: 'img\digits\d4096.png', 8192: 'img\digits\d8192.png'}
    for i in digits:
        digits[i] = load_image(digits[i])

    def __init__(self, *group, gamefon_class, mode=4):
        super().__init__(*group)
        self.digits = GameCycle.digits
        self.gamefon_class = gamefon_class
        self.mode = mode
        self.box = []
        for i in range(self.mode):
            self.box.append([0] * self.mode)
        print(self.box)
        self.box[random.randint(0, self.mode - 1)][random.randint(0, self.mode - 1)] = get_random_number() # ставим случайное число в случайное место
        self.x_bottom = self.gamefon_class.game_x_bottom()
        self.y_bottom = self.gamefon_class.game_y_bottom()

    def update(self, *args):
        for y in self.box:
            for x in y:
                if x in self.digits:
                    y_pos = self.box.index(y) + 1
                    x_pos = y.index(x) + 1
                    screen.blit(self.digits[x], (self.x_bottom + 15 * x_pos + 100 * (x_pos - 1),
                                                 self.y_bottom + 15 * y_pos + 100 * (y_pos - 1)))


GameGroup = pygame.sprite.Group()


GameFons = GameFon()
Cycle = GameCycle(gamefon_class=GameFons, mode=size_of_map)

GameGroup.add(GameFons, Cycle)