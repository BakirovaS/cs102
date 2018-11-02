# -*- coding: utf-8 -*-
import random
import pygame
from pygame.locals import *
from copy import deepcopy


class GameOfLife:

    def __init__(self, width=640, height=480, cell_size=10, speed=10):
        self.width = width
        self.height = height
        self.cell_size = cell_size

        # Устанавливаем размер окна
        self.screen_size = width, height
        # Создание нового окна
        self.screen = pygame.display.set_mode(self.screen_size)

        # Вычисляем количество ячеек по вертикали и горизонтали
        self.cell_width = self.width // self.cell_size
        self.cell_height = self.height // self.cell_size

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self):
        """ Отрисовать сетку """
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'),
                    (0, y), (self.width, y))

    def run(self):
        """ Запустить игру """
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))

        # Создание списка клеток
        self.clist = self.cell_list()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()

            # Отрисовка списка клеток
            # Выполнение одного шага игры (обновление состояния ячеек)
            self.draw_cell_list(self.clist)
            self.update_cell_list(self.clist)
            
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize = True):
        """ Создание списка клеток.
        :param randomize: Если True, то создается список клеток, где
        каждая клетка равновероятно может быть живой (1) или мертвой (0).
        :return: Список клеток, представленный в виде матрицы
        """
        self.clist = [[0 for i in range(self.cell_width)] for _ in range(self.cell_height)]

        if randomize:
            for i in range(self.cell_height):
                for j in range(self.cell_width):
                    self.clist[i][j] = random.randint(0, 1)
 
        return self.clist

    def draw_cell_list(self, clist):
        """ Отображение списка клеток
        :param rects: Список клеток для отрисовки, представленный в виде матрицы
        """
        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if clist[i][j]:
                    pygame.draw.rect(self.screen, pygame.Color('green'), 
                        (j * self.cell_size + 1, i * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), 
                        (j * self.cell_size + 1, i * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1))




    def get_neighbours(self, cell):
        """ Вернуть список соседей для указанной ячейки
        :param cell: Позиция ячейки в сетке, задается кортежем вида (row, col)
        :return: Одномерный список ячеек, смежных к ячейке cell
        """
        neighbours = []
        row, col = cell

        for i in range(max(0, row - 1), min(self.cell_height, row + 2)):
            for j in range(max(0, col - 1), min(self.cell_width, col + 2)):
                if (i == row and j == col):
                    continue
                neighbours.append(self.clist[i][j])

        return neighbours

    def update_cell_list(self, cell_list):
        """ Выполнить один шаг игры.
        Обновление всех ячеек происходит одновременно. Функция возвращает
        новое игровое поле.
        :param cell_list: Игровое поле, представленное в виде матрицы
        :return: Обновленное игровое поле
        """
        new_clist = deepcopy(self.clist)

        for i in range(self.cell_height):
            for j in range(self.cell_width):
                summ = sum(self.get_neighbours((i, j)))
                if self.clist[i][j]:
                    if not(summ == 3 or summ == 2) :
                        new_clist[i][j] = 0
                else:
                    if summ == 3:
                        new_clist[i][j] = 1

        self.clist = new_clist

        return self.clist

if __name__ == '__main__':
    game = GameOfLife(320, 240, 20)
    game.run()