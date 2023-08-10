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
            vr_sp = []
            for j in range(self.mode):
                vr_sp.append([0, True])
            self.box.append(vr_sp)
        #self.box[0] = [[2, True], [2, True], [2, True], [2, True]]
        #self.box[2] = [[2, True], [2, True], [2, True], [2, True]]
        #self.box[3] = [[4, True], [4, True], [4, True], [4, True]]
        #print(self.box)
        self.box[random.randint(0, self.mode - 1)][random.randint(0, self.mode - 1)][0] = get_random_number() # ставим случайное число в случайное место
        self.x_bottom = self.gamefon_class.game_x_bottom()
        self.y_bottom = self.gamefon_class.game_y_bottom()

    def update(self, *args):
        #print(args, args[0], args[0].type)
        sames_sp = True
        keys = pygame.key.get_pressed()
        is_pressed = False
        if args and args[0].type == pygame.KEYDOWN and keys[pygame.K_w]:
            is_pressed = True
            steps = 0
            give_for_draw = []
            for y_num in range(self.mode - 1):
                #print(y_num)
                for x_num in range(self.mode):
                    index = y_num + 1 # текущая строка
                    steps = 0
                    verh_kl = y_num
                    while index != 0:
                        if self.box[verh_kl][x_num][0] == 0 and self.box[index][x_num][0] != 0:  # верхняя клетка y_num
                            self.box[verh_kl][x_num] = self.box[index][x_num]  # возможно надо будет менять только число
                            self.box[index][x_num] = [0, True]
                            sames_sp = False
                        elif self.box[verh_kl][x_num] == self.box[index][x_num] and \
                                self.box[verh_kl][x_num][1] is True and self.box[index][x_num][0] != 0:
                            self.box[verh_kl][x_num] = [self.box[index][x_num][0] * 2, False]
                            self.box[index][x_num] = [0, True]
                            sames_sp = False
                        index -= 1
                        verh_kl -= 1

        elif args and args[0].type == pygame.KEYDOWN and keys[pygame.K_s]:
            is_pressed = True
            steps = 0
            give_for_draw = []
            for y_num in range(self.mode - 2, -1, -1): # ходим обратно от mode - 2 до 0 включительно
                for x_num in range(self.mode):
                    index = y_num # текущая строка
                    steps = 0
                    verh_kl = y_num + 1 # нижняя строка
                    while index != self.mode - 1:
                        if self.box[verh_kl][x_num][0] == 0 and self.box[index][x_num][0] != 0:  # верхняя клетка y_num
                            self.box[verh_kl][x_num] = self.box[index][x_num]  # возможно надо будет менять только число
                            self.box[index][x_num] = [0, True]
                            sames_sp = False
                        elif self.box[verh_kl][x_num] == self.box[index][x_num] and \
                                self.box[verh_kl][x_num][1] is True and self.box[index][x_num][0] != 0:
                            self.box[verh_kl][x_num] = [self.box[index][x_num][0] * 2, False]
                            self.box[index][x_num] = [0, True]
                            sames_sp = False
                        index += 1
                        verh_kl += 1

        elif args and args[0].type == pygame.KEYDOWN and keys[pygame.K_a]:
            is_pressed = True
            steps = 0
            give_for_draw = []
            for y_num in range(self.mode):
                #print(y_num)
                for x_num in range(self.mode - 1):
                    index = x_num + 1 # текущая строка
                    steps = 0
                    verh_kl = x_num
                    while index != 0:
                        if self.box[y_num][verh_kl][0] == 0 and self.box[y_num][index][0] != 0:  # верхняя клетка y_num
                            self.box[y_num][verh_kl] = self.box[y_num][index] # возможно надо будет менять только число
                            self.box[y_num][index] = [0, True]
                            sames_sp = False
                        elif self.box[y_num][verh_kl] == self.box[y_num][index] and \
                                self.box[y_num][verh_kl][1] is True and self.box[y_num][index][0] != 0:
                            self.box[y_num][verh_kl] = [self.box[y_num][index][0] * 2, False]
                            self.box[y_num][index] = [0, True]
                            sames_sp = False
                        index -= 1
                        verh_kl -= 1

        elif args and args[0].type == pygame.KEYDOWN and keys[pygame.K_d]:
            is_pressed = True
            steps = 0
            give_for_draw = []
            for y_num in range(self.mode):  # ходим обратно от mode - 2 до 0 включительно
                for x_num in range(self.mode - 2, -1, -1):
                    index = x_num  # текущая строка
                    steps = 0
                    verh_kl = x_num + 1  # нижняя строка
                    while index != self.mode - 1:
                        if self.box[y_num][verh_kl][0] == 0 and self.box[y_num][index][0] != 0:  # верхняя клетка y_num
                            self.box[y_num][verh_kl] = self.box[y_num][index]  # возможно надо будет менять только число
                            self.box[y_num][index] = [0, True]
                            sames_sp = False
                        elif self.box[y_num][verh_kl] == self.box[y_num][index] and \
                                self.box[y_num][verh_kl][1] is True and self.box[y_num][index][0] != 0:
                            self.box[y_num][verh_kl] = [self.box[y_num][index][0] * 2, False]
                            self.box[y_num][index] = [0, True]
                            sames_sp = False
                        index += 1
                        verh_kl += 1

        if is_pressed and not sames_sp:
            can_stick =[]
            for y in range(self.mode):
                for x in range(self.mode):
                    if self.box[y][x][0] == 0:
                        can_stick.append([y, x])
            if len(can_stick) != 0:
                pos = random.choice(can_stick)
                self.box[pos[0]][pos[1]][0] = get_random_number()

        # отрисовка в конце + все клетки True
        for y in range(self.mode):
            for x in range(self.mode):
                self.box[y][x][1] = True
                #print(x[0])
                if self.box[y][x][0] in self.digits:
                    #print(self.digits[x[0]])
                    y_pos = y + 1
                    x_pos = x + 1
                    screen.blit(self.digits[self.box[y][x][0]], (self.x_bottom + 15 * x_pos + 100 * (x_pos - 1),
                                                                 self.y_bottom + 15 * y_pos + 100 * (y_pos - 1)))


GameGroup = pygame.sprite.Group()


GameFons = GameFon()
Cycle = GameCycle(gamefon_class=GameFons, mode=size_of_map)

GameGroup.add(GameFons, Cycle)