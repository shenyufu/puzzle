# -*- coding: utf-8 -*-

import copy
import datetime
from table import table_size, brick_size, tables, bricks


def print_puzzle(table, no):
    print '== PUZZLE TABLE %s ==' % no
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
                    if brick_num == 0 or len(bricks) > 8:
                        print 'bricks:%s y:%s x:%s' % (brick_num, start_y, start_x), datetime.datetime.now()
                    result = place_brick(bricks, puzzle1, puzzle_size, brick_num + 1)
                    if result is not None:
                        return result
            else:
                continue


if __name__ == '__main__':
    i = raw_input('Choose puzzle number:')

    if i not in tables and i not in bricks:
        print "Can't find puzzle %s !" % i
    else:
        start = datetime.datetime.now()

        puzzle_table = tables[i]
        puzzle_brick = bricks[i]
        puzzle = []
        for y in range(table_size[1] + brick_size[1] - 1):
            row = []
            for x in range(table_size[0] + brick_size[0] - 1):
                if x < table_size[0] and y < table_size[1]:
                    if puzzle_table[y][x] == '#':
                        row.append([-1, '#'])
                    else:
                        row.append([-1, '-'])
                else:
                    row.append([0, '#'])
            puzzle.append(row)

        print_puzzle(puzzle, i)
        print "Total bricks %s pcs" % len(puzzle_brick)

        result = place_brick(puzzle_brick, puzzle, table_size, 0)
        print_puzzle(result, i)

        print 'Time cost: ', datetime.datetime.now() - start

    print '===== END ====='
