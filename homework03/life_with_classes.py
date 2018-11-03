# -*- coding: utf-8 -*-
import pygame
import random
from pygame.locals import *
from pprint import pprint as pp
from copy import deepcopy

class GameOfLife:
    def __init__(self, width=640, height=480, cell_size=10, speed=1):
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

        self.grid = self.cell_list()

        # Скорость протекания игры
        self.speed = speed

    def draw_grid(self):
        for x in range(0, self.width, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (
                x, 0), (x, self.height))
        for y in range(0, self.height, self.cell_size):
            pygame.draw.line(self.screen, pygame.Color('black'), (
                0, y), (self.width, y))

    def run(self):
        pygame.init()
        clock = pygame.time.Clock()
        pygame.display.set_caption('Game of Life')
        self.screen.fill(pygame.Color('white'))
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
            self.draw_grid()
            self.draw_cell_list()
            self.clist.update()
            pygame.display.flip()
            clock.tick(self.speed)
        pygame.quit()

    def cell_list(self, randomize = True):

        self.clist = CellList(self.cell_width, self.cell_height, randomize)
        self.grid = self.clist.grid
        return self.grid

    def draw_cell_list(self):

        for i in range(self.cell_height):
            for j in range(self.cell_width):
                if self.grid[i][j].alive:
                    pygame.draw.rect(self.screen, pygame.Color('green'), 
                        (j * self.cell_size + 1, i * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('white'), 
                        (j * self.cell_size + 1, i * self.cell_size + 1, self.cell_size - 1, self.cell_size - 1))                


class Cell:
    def __init__(self, row, col, state=0):
        self.alive = state
        self.row = row
        self.col = col

    def is_alive(self):
        return self.alive


class CellList:
    def __init__(self, nrows, ncols, randomize=True):
        self.nrows = nrows
        self.ncols = ncols
        if (randomize):
            self.grid = [[Cell(i, j, random.randint(0, 1))
                          for j in range(ncols)]
                         for i in range(nrows)]
        else:
            self.grid = [[Cell(i, j, 0)
                          for j in range(ncols)]
                         for i in range(nrows)]

    def get_neighbours(self, cell):
        neighbours = []
        row, col = cell.row, cell.col

        for i in range(max(0, row - 1), min(self.nrows, row + 2)):
            for j in range(max(0, col - 1), min(self.ncols, col + 2)):
                if (i == row and j == col):
                    continue
                neighbours.append(self.grid[i][j])


        return neighbours

    def update(self):
        new_grid = deepcopy(self.grid)

        for cell in self:
            neighbours = self.get_neighbours(cell)
            summ = sum(c.is_alive() for c in neighbours)
            if cell.is_alive():
                if not(summ == 3 or summ == 2):
                        new_grid[cell.row][cell.col].alive = 0
            else:
                if summ == 3:
                    new_grid[cell.row][cell.col].alive = 1

        self.grid = new_grid
        return self

    @classmethod
    def from_file(cls, filename):
        grid = []
        with open(filename) as f:
            for i, line in enumerate(f):
                grid.append([Cell(i, j, int(c))
                             for j, c in enumerate(line) if c in '01'])
        clist = cls(len(grid), len(grid[0]), False)
        clist.grid = grid
        return clist

    def __iter__(self):
        self.i_cnt, self.j_cnt = 0, 0
        return self

    def next(self):
        if (self.i_cnt == self.nrows):
            raise StopIteration

        cell = self.grid[self.i_cnt][self.j_cnt]
        self.j_cnt += 1
        if self.j_cnt == self.ncols:
            self.i_cnt += 1
            self.j_cnt = 0

        return cell

    def __str__(self):
        str = ""
        for i in range(self.nrows):
            for j in range(self.ncols):
                if (self.grid[i][j].alive):
                    str += '1 '
                else:
                    str += '0 '
            str += '\n'
        return str




if __name__ == '__main__':
    game = GameOfLife(320, 240, 40)
    game.run()