# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku/

import time

def solve(board):
    d = {
        0: [[], [], [], [], [], [], [], [], []],  # Row
        1: [[], [], [], [], [], [], [], [], []],  # Col
        2: [[], [], [], [], [], [], [], [], []]   # Box
    }

    for y in range(9):
        for x in range(9):
            if board[y][x] == '.':
                continue

            if board[y][x] in d[0][y] or \
                board[y][x] in d[1][x] or \
                board[y][x] in d[2][(y // 3) * 3 + (x // 3)]:
                    return False

            d[0][y].append(board[y][x])
            d[1][x].append(board[y][x])
            d[2][(y // 3) * 3 + (x // 3)].append(board[y][x])

    return True