import sys
import pygame
import os
import random

from configfile import screen, size_of_map, clock, FPS


# функция для подгрузки изображений
def load_image(name, colorkey=None):
    fullname = os.path.join('data', name)
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


def get_random_number():
    chanse = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
    return random.choice(chanse)


def draw_digit(args):
    # [sprites, {'x_bottom': int, 'y_bottom': int},
    # {'map_img': self.map_image, 'map_pos': self.map_pos, 'kletka_img': self.kletka_image},
    # button, True, [static_digits], {'nominal': int, start_pos: [y, x], plusing_pos: False, final_pos: [y, x]}, ...]
    sprites = args.pop(0)
    bottoms = args.pop(0)
    drawing_map_odj = args.pop(0)
    button = args.pop(0)
    is_static_digits = args.pop(0)
    static_digits = []
    if is_static_digits:
        static_digits = args.pop(0)
    while len(args) != 0:
        screen.blit(drawing_map_odj['map_img'], drawing_map_odj['map_pos'])
        for x in range(1, size_of_map + 1):
            for y in range(1, size_of_map + 1):
                screen.blit(drawing_map_odj['kletka_img'], (bottoms['x'] + 15 * x + 100 * (x - 1),
                                                            bottoms['y'] + 15 * y + 100 * (y - 1)))
        if is_static_digits:
            for static_digit in static_digits:
                #print(static_digit['final_pos'], static_digit['start_pos'] == static_digit['final_pos'])
                y_pos = static_digit['start_pos'][0] + 1
                x_pos = static_digit['start_pos'][1] + 1
                screen.blit(sprites[static_digit['nominal']], (bottoms['x'] + 15 * x_pos + 100 * (x_pos - 1),
                                                               bottoms['y'] + 15 * y_pos + 100 * (y_pos - 1)))
        if button == 'w':
            for digit in args:
                if digit['start_pos'][0] != digit['final_pos'][0]:
                    digit['start_pos'][0] = round(digit['start_pos'][0] - 0.1, 1) # округление из-за особенностей хранения чисел в pyton
                    y_pos = digit['start_pos'][0] + 1
                    x_pos = digit['start_pos'][1] + 1
                    screen.blit(sprites[digit['nominal']], (bottoms['x'] + 15 * x_pos + 100 * (x_pos - 1),
                                                            bottoms['y'] + 15 * y_pos + 100 * (y_pos - 1)))
                if digit['start_pos'][0] == digit['final_pos'][0]:
                    if digit['plusing_pos']:
                        digit['nominal'] *= 2
                    is_static_digits = True
                    static_digits.append(digit)
                    args.remove(digit)
        elif button == 's':
            for digit in args:
                if digit['start_pos'][0] != digit['final_pos'][0]:
                    digit['start_pos'][0] = round(digit['start_pos'][0] + 0.1, 1) # округление из-за особенностей хранения чисел в pyton
                    y_pos = digit['start_pos'][0] + 1
                    x_pos = digit['start_pos'][1] + 1
                    screen.blit(sprites[digit['nominal']], (bottoms['x'] + 15 * x_pos + 100 * (x_pos - 1),
                                                            bottoms['y'] + 15 * y_pos + 100 * (y_pos - 1)))
                if digit['start_pos'][0] == digit['final_pos'][0]:
                    if digit['plusing_pos']:
                        digit['nominal'] *= 2
                    is_static_digits = True
                    static_digits.append(digit)
                    args.remove(digit)
        elif button == 'a':
            for digit in args:
                if digit['start_pos'][1] != digit['final_pos'][1]:
                    digit['start_pos'][1] = round(digit['start_pos'][1] - 0.1, 1) # округление из-за особенностей хранения чисел в pyton
                    y_pos = digit['start_pos'][0] + 1
                    x_pos = digit['start_pos'][1] + 1
                    screen.blit(sprites[digit['nominal']], (bottoms['x'] + 15 * x_pos + 100 * (x_pos - 1),
                                                            bottoms['y'] + 15 * y_pos + 100 * (y_pos - 1)))
                if digit['start_pos'][1] == digit['final_pos'][1]:
                    if digit['plusing_pos']:
                        digit['nominal'] *= 2
                    is_static_digits = True
                    static_digits.append(digit)
                    args.remove(digit)
        elif button == 'd':
            for digit in args:
                if digit['start_pos'][1] != digit['final_pos'][1]:
                    digit['start_pos'][1] = round(digit['start_pos'][1] + 0.1, 1) # округление из-за особенностей хранения чисел в pyton
                    y_pos = digit['start_pos'][0] + 1
                    x_pos = digit['start_pos'][1] + 1
                    screen.blit(sprites[digit['nominal']], (bottoms['x'] + 15 * x_pos + 100 * (x_pos - 1),
                                                            bottoms['y'] + 15 * y_pos + 100 * (y_pos - 1)))
                if digit['start_pos'][1] == digit['final_pos'][1]:
                    if digit['plusing_pos']:
                        digit['nominal'] *= 2
                    is_static_digits = True
                    static_digits.append(digit)
                    args.remove(digit)
        pygame.display.flip()
        clock.tick(FPS)
