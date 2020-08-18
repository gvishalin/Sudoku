import random
import math

q = int(math.sqrt(9))

def rand_int(n):
    return int((random.random()*n+1))



def unused_box(bo, row, col, n):
    for i in range(q):
        for j in range(q):
            if bo[row+i][col+j] == n:
                return False
    return True


def fill_box(bo, row, col):
    n = rand_int(9)

    for i in range(q):
        for j in range(q):
            while not(unused_box(bo, row, col, n)):
                n = rand_int(9)

            bo[row+i][col+j] = n



def check_safe(bo, row, col, n):
    return (unused_row(bo, row, n) and unused_col(bo, col, n) and unused_box(bo, row-row%q, col-col%q, n))


def unused_row(bo, row, n):
    for i in range(9):
        if bo[row][i] == n:
            return False
    return True


def unused_col(bo, col, n):
    for i in range(9):
        if bo[i][col] == n:
            return False
    return True


def fill_dia(bo):
    i = 0
    while i < 9:
        fill_box(bo, i, i)
        i = i + q


def fill_body(bo, i, j):
    if j >= 9 and i < 8:
        i = i+1
        j = 0
    if i >= 9 and j >= 9:
        return True
    if i < q:
        if j < q:
            j = q
    elif i < (9-q):
        if j == int(i/q)*q:
            j = j + q
    else:
        if j == (9-q):
            i = i + 1
            j = 0
            if i >= 9:
                return True

    for num in range(1, 10):
        if check_safe(bo, i, j, num):
            bo[i][j] = num
            if fill_body(bo, i, j+1):
                return True

            bo[i][j] = 0
    return False


def remove_digi(bo, k):
    count = k
    while count != 0:
        cell = rand_int(81)
        i = cell // 9
        j = cell % 9
        if j != 0:
            j = j - 1

        if bo[i][j] != 0:
            count = count - 1
            bo[i][j] = 0


def fill_values(bo, k):
    fill_dia(bo)
    fill_body(bo, 0, q)
    remove_digi(bo, k)


def print_board(bo):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("------------------------")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

board = []

for i in range(9):
    a = []
    for j in range(9):
        a.append(0)
    board.append(a)

p = int(input("Give number of elements to be removed:"))

fill_values(board, p)
print_board(board)