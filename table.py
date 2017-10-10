# -*- coding: utf-8 -*-

table_size = (6, 6)
brick_size = (2, 2)

puzzles = dict()

puzzles['1'] = {
    'tables': (
        ('#', '#', '#', '#', '#', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '#', '#', '#', '#', '#'),
    ),
    'bricks': (
        (('O', '-'), ('-', '-')),
        (('R', '-'), ('-', '-')),
        (('R', 'R'), ('R', 'R')),
        (('O', 'O'), ('O', 'O')),
        (('O', 'O'), ('-', '-')),
        (('R', 'R'), ('-', '-')),
        (('R', 'R'), ('-', '-')),
        (('O', 'O'), ('-', '-')),
    )
}

puzzles['2'] = {
    'tables': (
        ('#', '#', '#', '#', '#', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '#', '#', '#', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '#', '#', '#', '#'),
        ('#', '-', '-', '-', '-', '#'),
    ),
    'bricks': (
        (('Y', 'Y'), ('Y', '-')),
        (('R', 'R'), ('-', '-')),
        (('R', '-'), ('-', '-')),
        (('R', '-'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
        (('Y', '-'), ('Y', 'Y')),
        (('R', 'R'), ('-', '-')),
    )
}

puzzles['3'] = {
    'tables': (
        ('#', '#', '#', '#', '#', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '#', '#', '#', '#', '#'),
    ),
    'bricks': (
        (('G', 'G'), ('G', '-')),
        (('Y', '-'), ('-', '-')),
        (('R', '-'), ('-', '-')),
        (('G', '-'), ('-', '-')),
        (('G', 'G'), ('-', '-')),
        (('R', '-'), ('-', '-')),
        (('Y', 'Y'), ('-', 'Y')),
        (('R', 'R'), ('R', 'R')),
    )
}

puzzles['4'] = {
    'tables': (
        ('#', '#', '#', '#', '#', '#'),
        ('#', '#', '-', '-', '#', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '#', '-', '-', '#', '#'),
        ('#', '#', '-', '-', '#', '#'),
    ),
    'bricks': (
        (('G', 'G'), ('G', 'G')),
        (('G', 'G'), ('-', '-')),
        (('C', 'C'), ('-', '-')),
        (('C', 'C'), ('-', '-')),
        (('B', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
        (('C', 'C'), ('-', '-')),
        (('B', 'B'), ('-', '-')),
    )
}

puzzles['5'] = {
    'tables': (
        ('#', '#', '#', '#', '#', '#'),
        ('#', '#', '-', '-', '#', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '#', '-', '-', '#', '#'),
    ),
    'bricks': (
        (('Y', '-'), ('-', '-')),
        (('R', '-'), ('-', '-')),
        (('-', 'Y'), ('Y', 'Y')),
        (('O', '-'), ('O', '-')),
        (('O', '-'), ('O', '-')),
        (('Y', '-'), ('-', '-')),
        (('R', 'R'), ('R', 'R')),
        (('Y', '-'), ('-', '-')),
        (('O', '-'), ('-', '-')),
    )
}

puzzles['6'] = {
    'tables': (
        ('-', '-', '#', '#', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '-', '#', '#', '-', '#'),
        ('#', '-', '#', '#', '-', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '#', '#', '-', '-'),
    ),
    'bricks': (
        (('G', '-'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
        (('G', '-'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
        (('G', '-'), ('-', '-')),
        (('G', 'G'), ('G', '-')),
        (('-', 'G'), ('G', 'G')),
        (('Y', 'Y'), ('-', 'Y')),
        (('Y', '-'), ('Y', 'Y')),
        (('-', 'Y'), ('Y', 'Y')),
        (('G', '-'), ('G', 'G')),
    )
}

puzzles['7'] = {
    'tables': (
        ('#', '#', '#', '#', '#', '#'),
        ('#', '#', '-', '-', '#', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
    ),
    'bricks': (
        (('B', '-'), ('-', '-')),
        (('B', 'B'), ('-', '-')),
        (('-', 'B'), ('B', 'B')),
        (('C', '-'), ('C', '-')),
        (('C', '-'), ('C', '-')),
        (('B', '-'), ('-', '-')),
        (('G', 'G'), ('G', 'G')),
        (('G', 'G'), ('-', '-')),
        (('G', '-'), ('-', '-')),
    )
}

puzzles['8'] = {
    'tables': (
        ('#', '#', '#', '#', '#', '#'),
        ('#', '-', '#', '#', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
    ),
    'bricks': (
        (('C', 'C'), ('-', '-')),
        (('C', '-'), ('C', 'C')),
        (('G', '-'), ('G', '-')),
        (('Y', 'Y'), ('-', '-')),
        (('G', '-'), ('G', 'G')),
        (('Y', 'Y'), ('-', 'Y')),
        (('Y', '-'), ('-', '-')),
        (('C', '-'), ('-', '-')),
        (('G', '-'), ('-', '-')),
    )
}

puzzles['9'] = {
    'tables': (
        ('#', '-', '-', '-', '-', '#'),
        ('#', '#', '-', '-', '#', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '#', '-', '-', '#', '#'),
        ('#', '-', '-', '-', '-', '#'),
    ),
    'bricks': (
        (('R', 'R'), ('R', 'R')),
        (('Y', 'Y'), ('Y', 'Y')),
        (('R', 'R'), ('R', '-')),
        (('-', 'Y'), ('Y', 'Y')),
        (('B', 'B'), ('-', 'B')),
        (('B', '-'), ('B', 'B')),
        (('B', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
        (('R', '-'), ('-', '-')),
    )
}

puzzles['10'] = {
    'tables': (
        ('#', '#', '#', '#', '#', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '-', '-', '-', '-', '#'),
    ),
    'bricks': (
        (('B', 'B'), ('B', 'B')),
        (('-', 'B'), ('B', 'B')),
        (('B', 'B'), ('-', '-')),
        (('G', '-'), ('G', '-')),
        (('C', '-'), ('C', '-')),
        (('G', 'G'), ('-', '-')),
        (('C', '-'), ('-', '-')),
        (('C', '-'), ('-', '-')),
        (('C', '-'), ('-', '-')),
        (('C', '-'), ('-', '-')),
        (('G', '-'), ('-', '-')),
        (('G', '-'), ('-', '-')),
        (('G', '-'), ('-', '-')),
        (('C', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
    )
}

puzzles['11'] = {
    'tables': (
        ('#', '#', '-', '-', '#', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '-', '-', '-', '-', '-'),
        ('#', '#', '-', '-', '#', '#'),
        ('#', '-', '-', '-', '-', '#'),
    ),
    'bricks': (
        (('-', 'R'), ('R', 'R')),
        (('-', 'C'), ('C', 'C')),
        (('B', '-'), ('B', 'B')),
        (('G', 'G'), ('G', '-')),
        (('R', 'R'), ('-', 'R')),
        (('G', '-'), ('G', 'G')),
        (('G', '-'), ('G', '-')),
        (('C', 'C'), ('-', '-')),
        (('R', '-'), ('-', '-')),
    )
}

puzzles['12'] = {
    'tables': (
        ('-', '-', '#', '#', '#', '#'),
        ('-', '-', '-', '#', '-', '-'),
        ('#', '#', '-', '-', '-', '-'),
        ('#', '-', '-', '-', '-', '-'),
        ('#', '-', '-', '#', '#', '#'),
        ('-', '-', '-', '#', '#', '#'),
    ),
    'bricks': (
        (('B', 'B'), ('B', 'B')),
        (('G', '-'), ('G', 'G')),
        (('G', 'G'), ('-', 'G')),
        (('Y', '-'), ('Y', 'Y')),
        (('B', 'B'), ('-', '-')),
        (('Y', 'Y'), ('-', '-')),
        (('G', '-'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
    )
}

puzzles['13'] = {
    'tables': (
        ('#', '#', '#', '#', '#', '#'),
        ('#', '-', '#', '-', '#', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
    ),
    'bricks': (
        (('B', 'B'), ('B', 'B')),
        (('C', 'C'), ('-', 'C')),
        (('-', 'Y'), ('Y', 'Y')),
        (('Y', '-'), ('Y', '-')),
        (('B', '-'), ('B', '-')),
        (('Y', 'Y'), ('-', '-')),
        (('C', '-'), ('C', '-')),
        (('B', 'B'), ('-', '-')),
        (('C', 'C'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
    )
}

puzzles['14'] = {
    'tables': (
        ('-', '-', '-', '-', '#', '#'),
        ('#', '-', '-', '#', '#', '#'),
        ('#', '-', '-', '-', '#', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '-', '-', '-', '#', '#'),
        ('#', '#', '-', '-', '-', '#'),
    ),
    'bricks': (
        (('G', 'G'), ('G', '-')),
        (('-', 'G'), ('G', 'G')),
        (('C', 'C'), ('-', 'C')),
        (('C', 'C'), ('-', '-')),
        (('B', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
        (('C', '-'), ('-', '-')),
        (('C', '-'), ('-', '-')),
        (('G', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
        (('C', '-'), ('-', '-')),
        (('C', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
    )
}

puzzles['15'] = {
    'tables': (
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '#', '-', '-', '#', '#'),
    ),
    'bricks': (
        (('R', 'R'), ('R', 'R')),
        (('Y', 'Y'), ('Y', 'Y')),
        (('O', 'O'), ('O', 'O')),
        (('-', 'Y'), ('Y', 'Y')),
        (('O', '-'), ('O', 'O')),
        (('O', 'O'), ('-', '-')),
        (('R', 'R'), ('-', '-')),
        (('Y', 'Y'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
        (('O', '-'), ('-', '-')),
        (('O', '-'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
    )
}

puzzles['16'] = {
    'tables': (
        ('-', '#', '#', '#', '#', '-'),
        ('-', '-', '#', '#', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
    ),
    'bricks': (
        (('B', 'B'), ('B', 'B')),
        (('R', 'R'), ('-', 'R')),
        (('R', '-'), ('R', 'R')),
        (('Y', '-'), ('Y', 'Y')),
        (('B', 'B'), ('-', 'B')),
        (('R', 'R'), ('R', '-')),
        (('B', 'B'), ('-', '-')),
        (('Y', '-'), ('Y', '-')),
        (('R', '-'), ('R', '-')),
        (('B', '-'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
        (('R', '-'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
    )
}

puzzles['17'] = {
    'tables': (
        ('#', '#', '-', '-', '#', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('-', '-', '#', '#', '-', '-'),
        ('-', '-', '#', '#', '-', '-'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '#', '-', '-', '#', '#'),
    ),
    'bricks': (
        (('G', 'G'), ('G', 'G')),
        (('C', '-'), ('C', 'C')),
        (('G', 'G'), ('-', 'G')),
        (('-', 'R'), ('R', 'R')),
        (('G', '-'), ('G', '-')),
        (('C', '-'), ('-', '-')),
        (('C', '-'), ('-', '-')),
        (('R', '-'), ('-', '-')),
        (('R', '-'), ('-', '-')),
        (('R', '-'), ('-', '-')),
    )
}

puzzles['18'] = {
    'tables': (
        ('#', '#', '#', '#', '#', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '#', '#', '#', '#', '#'),
    ),
    'bricks': (
        (('R', 'R'), ('R', 'R')),
        (('B', 'B'), ('-', 'B')),
        (('B', 'B'), ('B', '-')),
        (('-', 'Y'), ('Y', 'Y')),
        (('R', '-'), ('R', '-')),
        (('B', 'B'), ('-', '-')),
        (('Y', 'Y'), ('-', '-')),
        (('R', '-'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
        (('R', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
    )
}

puzzles['19'] = {
    'tables': (
        ('#', '#', '-', '-', '-', '-'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '#', '-', '-', '#', '#'),
    ),
    'bricks': (
        (('R', 'R'), ('R', 'R')),
        (('Y', 'Y'), ('Y', 'Y')),
        (('-', 'B'), ('B', 'B')),
        (('Y', '-'), ('Y', 'Y')),
        (('R', '-'), ('R', 'R')),
        (('R', 'R'), ('-', '-')),
        (('R', 'R'), ('-', '-')),
        (('B', 'B'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
    )
}

puzzles['20'] = {
    'tables': (
        ('#', '#', '-', '-', '-', '#'),
        ('#', '#', '-', '-', '-', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '#', '-', '-', '#', '-'),
        ('-', '#', '-', '-', '#', '-'),
    ),
    'bricks': (
        (('B', 'B'), ('B', 'B')),
        (('-', 'G'), ('G', 'G')),
        (('B', 'B'), ('-', 'B')),
        (('-', 'C'), ('C', 'C')),
        (('G', '-'), ('G', 'G')),
        (('B', '-'), ('B', '-')),
        (('C', 'C'), ('-', '-')),
        (('G', 'G'), ('-', '-')),
        (('C', '-'), ('C', '-')),
        (('G', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
    )
}


puzzles['21'] = {
    'tables': (
        ('-', '#', '#', '#', '#', '#'),
        ('-', '-', '-', '-', '#', '#'),
        ('-', '-', '-', '-', '-', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
    ),
    'bricks': (
        (('O', 'O'), ('O', 'O')),
        (('O', 'O'), ('O', '-')),
        (('-', 'R'), ('R', 'R')),
        (('R', '-'), ('R', 'R')),
        (('Y', 'Y'), ('-', 'Y')),
        (('Y', '-'), ('Y', 'Y')),
        (('Y', 'Y'), ('Y', '-')),
        (('R', '-'), ('R', 'R')),
        (('Y', '-'), ('-', '-')),
        (('O', '-'), ('-', '-')),
        (('O', '-'), ('-', '-')),
    )
}

puzzles['22'] = {
    'tables': (
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '#', '#', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '#', '-', '-', '#', '#'),
        ('-', '-', '-', '-', '#', '#'),
    ),
    'bricks': (
        (('-', 'R'), ('R', 'R')),
        (('R', 'R'), ('R', '-')),
        (('B', '-'), ('B', 'B')),
        (('C', 'C'), ('-', '-')),
        (('C', '-'), ('C', '-')),
        (('B', '-'), ('B', '-')),
        (('C', 'C'), ('-', '-')),
        (('B', '-'), ('B', '-')),
        (('C', '-'), ('C', '-')),
        (('B', '-'), ('-', '-')),
        (('R', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
    )
}

puzzles['23'] = {
    'tables': (
        ('#', '#', '#', '#', '#', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('-', '-', '-', '-', '-', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '-', '-', '-', '-', '-'),
        ('#', '-', '-', '-', '-', '-'),
    ),
    'bricks': (
        (('G', 'G'), ('-', 'G')),
        (('G', '-'), ('G', 'G')),
        (('O', '-'), ('O', 'O')),
        (('O', 'O'), ('O', '-')),
        (('O', '-'), ('O', '-')),
        (('O', 'O'), ('-', '-')),
        (('C', 'C'), ('C', '-')),
        (('C', 'C'), ('C', '-')),
        (('C', '-'), ('C', '-')),
        (('G', '-'), ('-', '-')),
    )
}

puzzles['24'] = {
    'tables': (
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '-', '-', '-', '-', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '-', '#', '#', '-', '#'),
    ),
    'bricks': (
        (('Y', 'Y'), ('Y', 'Y')),
        (('Y', 'Y'), ('Y', '-')),
        (('-', 'Y'), ('Y', 'Y')),
        (('R', 'R'), ('R', '-')),
        (('R', 'R'), ('-', 'R')),
        (('O', 'O'), ('-', '-')),
        (('O', 'O'), ('-', '-')),
        (('O', 'O'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
        (('R', '-'), ('-', '-')),
        (('R', '-'), ('-', '-')),
    )
}

puzzles['25'] = {
    'tables': (
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '-', '-'),
    ),
    'bricks': (
        (('B', 'B'), ('B', 'B')),
        (('-', 'B'), ('B', 'B')),
        (('G', '-'), ('G', 'G')),
        (('C', '-'), ('C', '-')),
        (('B', 'B'), ('-', '-')),
        (('G', 'G'), ('-', '-')),
        (('C', '-'), ('C', '-')),
        (('B', 'B'), ('-', '-')),
        (('G', '-'), ('G', '-')),
        (('G', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
        (('C', '-'), ('-', '-')),
        (('C', '-'), ('-', '-')),
        (('C', '-'), ('-', '-')),
        (('G', '-'), ('-', '-')),
        (('C', '-'), ('-', '-')),
    )
}

puzzles['26'] = {
    'tables': (
        ('#', '#', '#', '#', '#', '-'),
        ('#', '#', '#', '-', '-', '-'),
        ('#', '-', '-', '-', '-', '-'),
        ('#', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
    ),
    'bricks': (
        (('B', 'B'), ('B', '-')),
        (('-', 'B'), ('B', 'B')),
        (('R', 'R'), ('R', 'R')),
        (('C', 'C'), ('-', 'C')),
        (('C', 'C'), ('-', '-')),
        (('C', '-'), ('C', '-')),
        (('B', 'B'), ('-', '-')),
        (('B', '-'), ('B', '-')),
        (('B', 'B'), ('-', '-')),
        (('R', '-'), ('R', '-')),
        (('R', '-'), ('-', '-')),
    )
}

puzzles['27'] = {
    'tables': (
        ('#', '#', '#', '#', '#', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '#', '#', '-', '-'),
    ),
    'bricks': (
        (('Y', 'Y'), ('Y', 'Y')),
        (('G', 'G'), ('G', 'G')),
        (('Y', 'Y'), ('Y', 'Y')),
        (('C', 'C'), ('-', 'C')),
        (('C', 'C'), ('C', '-')),
        (('G', 'G'), ('-', '-')),
        (('C', 'C'), ('-', '-')),
        (('G', 'G'), ('-', '-')),
        (('Y', '-'), ('-', '-')),
        (('C', '-'), ('-', '-')),
        (('G', '-'), ('-', '-')),
        (('G', '-'), ('-', '-')),
    )
}

puzzles['28'] = {
    'tables': (
        ('#', '-', '-', '-', '-', '#'),
        ('#', '-', '-', '-', '#', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '#', '-', '-', '-'),
        ('#', '-', '#', '#', '-', '-'),
        ('#', '-', '-', '-', '-', '#'),
    ),
    'bricks': (
        (('Y', 'Y'), ('Y', 'Y')),
        (('Y', 'Y'), ('Y', '-')),
        (('B', 'B'), ('-', 'B')),
        (('-', 'Y'), ('Y', 'Y')),
        (('G', 'G'), ('-', 'G')),
        (('Y', '-'), ('Y', '-')),
        (('B', 'B'), ('-', '-')),
        (('G', 'G'), ('-', '-')),
        (('B', 'B'), ('-', '-')),
        (('G', '-'), ('-', '-')),
    )
}

puzzles['29'] = {
    'tables': (
        ('#', '#', '#', '#', '#', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
    ),
    'bricks': (
        (('R', 'R'), ('R', 'R')),
        (('Y', '-'), ('Y', '-')),
        (('Y', '-'), ('Y', '-')),
        (('Y', '-'), ('Y', '-')),
        (('G', '-'), ('G', '-')),
        (('R', '-'), ('R', '-')),
        (('Y', '-'), ('Y', '-')),
        (('G', '-'), ('G', '-')),
        (('G', 'G'), ('-', '-')),
        (('Y', 'Y'), ('-', '-')),
        (('G', '-'), ('G', '-')),
        (('R', 'R'), ('-', '-')),
        (('R', 'R'), ('-', '-')),
        (('R', '-'), ('-', '-')),
        (('R', '-'), ('-', '-')),
    )
}

puzzles['30'] = {
    'tables': (
        ('#', '-', '-', '-', '-', '#'),
        ('-', '#', '-', '-', '#', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '#', '-', '-', '#', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
    ),
    'bricks': (
        (('C', 'C'), ('C', 'C')),
        (('G', 'G'), ('-', 'G')),
        (('G', '-'), ('G', 'G')),
        (('B', 'B'), ('B', '-')),
        (('B', '-'), ('B', '-')),
        (('B', '-'), ('B', '-')),
        (('C', '-'), ('C', '-')),
        (('C', '-'), ('C', '-')),
        (('C', 'C'), ('-', '-')),
        (('G', 'G'), ('-', '-')),
        (('G', 'G'), ('-', '-')),
        (('G', '-'), ('-', '-')),
        (('B', '-'), ('-', '-')),
        (('G', '-'), ('-', '-')),
    )
}

puzzles['31'] = {
    'tables': (
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '#', '#', '#', '#', '#'),
    ),
    'bricks': (
        (('O', 'O'), ('O', 'O')),
        (('O', '-'), ('O', 'O')),
        (('-', 'O'), ('O', 'O')),
        (('B', 'B'), ('-', 'B')),
        (('B', 'B'), ('B', '-')),
        (('B', 'B'), ('-', '-')),
        (('B', 'B'), ('-', '-')),
        (('B', 'B'), ('-', '-')),
        (('G', 'G'), ('-', '-')),
        (('G', '-'), ('G', '-')),
        (('G', '-'), ('G', '-')),
        (('G', 'G'), ('-', '-')),
    )
}

puzzles['32'] = {
    'tables': (
        ('-', '#', '#', '#', '#', '#'),
        ('-', '-', '-', '-', '-', '-'),
        ('#', '-', '-', '-', '-', '-'),
        ('#', '-', '-', '-', '-', '-'),
        ('#', '-', '-', '-', '-', '-'),
        ('#', '-', '-', '-', '-', '-'),
    ),
    'bricks': (
        (('Y', '-'), ('Y', 'Y')),
        (('R', 'R'), ('-', 'R')),
        (('-', 'Y'), ('Y', 'Y')),
        (('R', '-'), ('R', 'R')),
        (('R', 'R'), ('R', '-')),
        (('Y', 'Y'), ('Y', '-')),
        (('-', 'R'), ('R', 'R')),
        (('Y', 'Y'), ('-', 'Y')),
        (('B', '-'), ('B', '-')),
        (('R', '-'), ('-', '-')),
    )
}
