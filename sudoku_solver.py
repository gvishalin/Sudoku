# Example board
# 
# 9 0 3 0 0 8 4 0 0
# 0 5 0 1 0 7 0 0 3
# 6 8 7 3 0 2 9 0 0
# 0 0 0 6 0 0 0 0 0
# 5 3 8 2 0 0 0 0 0
# 1 0 2 0 0 4 0 9 0
# 3 0 0 9 0 6 0 7 0
# 7 2 6 8 5 1 0 4 0
# 0 0 0 4 0 3 2 5 0
# 


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, find):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0

    return False



def valid(bo, num, pos):
    # Checking row
    for i in range(9):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Checking column
    for i in range(9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Checking position in box
    box_x = pos[0] // 3
    box_y = pos[1] // 3

    for i in range(box_x*3, box_x*3 + 3):
        for j in range(box_y * 3, box_y*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def print_board(bo):
    print("Solved board:")
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


def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i, j) 

    return None


board = [] 

print("Give space seperated integers as input!")
print("Give each row in a seperate line")

# For user input 
for i in range(9): 
    a = input()
    board.append(a.split())

for i in range(9):
    for j in range(9):
        board[i][j] = int(board[i][j])

solve(board)
print_board(board)
