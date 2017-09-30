#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy

puzzle_size = (6, 6)
brick_size = (2, 2)

puzzle_table = (
    ('#', '#', '-', '-', '-', '-'),
    ('#', '-', '-', '-', '-', '#'),
    ('#', '-', '-', '-', '-', '#'),
    ('#', '-', '-', '-', '-', '#'),
    ('-', '-', '-', '-', '-', '-'),
    ('#', '#', '-', '-', '#', '#'),
)
bricks = (
    (('R', 'R'), ('-', '-')),
    (('R', 'R'), ('-', '-')),
    (('R', 'R'), ('R', 'R')),
    (('R', '-'), ('R', 'R')),
    (('B', 'B'), ('-', '-')),
    (('-', 'B'), ('B', 'B')),
    (('Y', '-'), ('Y', 'Y')),
    (('Y', 'Y'), ('Y', 'Y')),
    (('Y', '-'), ('-', '-')),
)


def print_puzzle(table):
    print '== PUZZLE TABLE =='
    for row in table:
        string = ''
        for bit in row:
            if not bit:
                string += '-'
            else:
                string += bit[1]
        print string


def check_puzzle(table):
    for row in table:
        for bit in row:
            if bit[1] == '!':
                return False

    len_y, len_x = len(table), len(table[0])
    for y in range(len_y):
        for x in range(len_x):
            if table[y][x][1] not in ('#', '-'):
                if y > 0 and (table[y][x][1] == table[y - 1][x][1] and table[y][x][0] != table[y - 1][x][0]):
                    return False
                if y < len_y - 1 and (table[y][x][1] == table[y + 1][x][1] and table[y][x][0] != table[y + 1][x][0]):
                    return False
                if x > 0 and (table[y][x][1] == table[y][x - 1][1] and table[y][x][0] != table[y][x - 1][0]):
                    return False
                if x < len_x - 1 and (table[y][x][1] == table[y][x + 1][1] and table[y][x][0] != table[y][x + 1][0]):
                    return False

    return True


def place_brick(bricks, puzzle, puzzle_size, brick_num):
    if not bricks:
        return
    brick = bricks[0]
    bricks = bricks[1:]

    for start_y in range(puzzle_size[1]):
        for start_x in range(puzzle_size[0]):
            puzzle1 = copy.deepcopy(puzzle)
            for y, row in enumerate(brick):
                for x, bit in enumerate(row):
                    if bit != '-':
                        if puzzle1[start_y + y][start_x + x][1] == '-':
                            puzzle1[start_y + y][start_x + x] = [brick_num, bit]
                        else:
                            puzzle1[start_y + y][start_x + x] = [brick_num, '!']
            if check_puzzle(puzzle1):
                if len(bricks) == 0:
                    return puzzle1
                else:
                    result = place_brick(bricks, puzzle1, puzzle_size, brick_num + 1)
                    if result is not None:
                        return result
            else:
                continue


if __name__ == '__main__':
    puzzle = []
    for y in range(puzzle_size[1] + brick_size[1] - 1):
        row = []
        for x in range(puzzle_size[0] + brick_size[0] - 1):
            if x < puzzle_size[0] and y < puzzle_size[1]:
                if puzzle_table[y][x] == '#':
                    row.append([-1, '#'])
                else:
                    row.append([-1, '-'])
            else:
                row.append([0, '#'])
        puzzle.append(row)

    print_puzzle(puzzle)

    result = place_brick(bricks, puzzle, puzzle_size, 0)
    print_puzzle(result)

    print 'END'
