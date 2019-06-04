import random
from copy import deepcopy

class Puzzle(object):
    matrix = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    end = [[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]
    undo_stack = []

    def __init__(self, matrix = "rnd", end = "default"):
        if matrix == "rnd":
            self.shuffle()
        else:
            self.matrix = matrix
        if not end == 'default':
            self.end = end

    def move(self, row, column):
        for i in range(row-1, row+2):
            for j in range(column-1, column+2):
                if 0 <= i <= 3 and 0 <= j <= 3 and not(row == i and column == j) and abs(row-i) != abs(column-j) and self.matrix[i][j] == 0:
                    self.undo_stack.append(deepcopy(self.matrix))
                    self.matrix[i][j] = self.matrix[row][column]
                    self.matrix[row][column] = 0
                    return

    def moves(self):
        for i in self.matrix:
            if 0 in i:
                row, column = self.matrix.index(i), i.index(0)
        ls = []
        for i in range(row-1, row+2):
            for j in range(column-1, column+2):
                if 0 <= i <= 3 and 0 <= j <= 3 and not(row == i and column == j) and abs(row-i) != abs(column-j):
                    t = deepcopy(self.matrix)
                    t[i][j], t[row][column] = t[row][column], t[i][j]
                    ls.append(t)
        return ls

        
    def shuffle(self):
        for _ in range(200):
            self.set(self.moves()[random.randint(0, len(self.moves())-1)])

    def get(self):
        return self.matrix

    def set(self, matrix):
        self.matrix = matrix

    def check(self):
        if self.matrix == self.end:
            return True
        return False

    def undo(self):
        if self.undo_stack:
            self.matrix = self.undo_stack.pop()
            return True
        return False

    def display(self):
        matrix = [[str(j) for j in i] for i in self.matrix]
        matrix = [[j.rjust(2) for j in i] for i in matrix]
        print('--------------------')
        print(' ' + matrix[0][0] + ' | ' + matrix[0][1] + ' | ' + matrix[0][2] + ' | ' + matrix[0][3] + ' |')
        print('--------------------')
        print(' ' + matrix[1][0] + ' | ' + matrix[1][1] + ' | ' + matrix[1][2] + ' | ' + matrix[1][3] + ' |')
        print('--------------------')
        print(' ' + matrix[2][0] + ' | ' + matrix[2][1] + ' | ' + matrix[2][2] + ' | ' + matrix[2][3] + ' |')
        print('--------------------')
        print(' ' + matrix[3][0] + ' | ' + matrix[3][1] + ' | ' + matrix[3][2] + ' | ' + matrix[3][3] + ' |')
        print('--------------------')