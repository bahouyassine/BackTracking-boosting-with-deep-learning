import random

def print_grid(arr):
    for row in arr:
        print(" ".join(str(num) if num != 0 else '0' for num in row))

def is_safe(arr, row, col, num):
    # Check if 'num' is not in row, column and current 3x3 box
    for x in range(9):
        if arr[row][x] == num or arr[x][col] == num:
            return False
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if arr[i + start_row][j + start_col] == num:
                return False
    return True

def fill_diagonal(arr):
    for i in range(0, 9, 3):
        fill_box(arr, i, i)

def fill_box(arr, row, col):
    num = 1
    for i in range(3):
        for j in range(3):
            while not is_safe(arr, row, col, num):
                num = random.randint(1, 9)
            arr[row + i][col + j] = num
            num = random.randint(1, 9)

def fill_remaining(arr, i, j):
    if j >= 9 and i < 8:
        i += 1
        j = 0
    if i >= 9 and j >= 9:
        return True
    if i < 3:
        if j < 3:
            j = 3
    elif i < 6:
        if j == int(i / 3) * 3:
            j += 3
    else:
        if j == 6:
            i += 1
            j = 0
            if i >= 9:
                return True
    for num in range(1, 10):
        if is_safe(arr, i, j, num):
            arr[i][j] = num
            if fill_remaining(arr, i, j + 1):
                return True
            arr[i][j] = 0
    return False

def remove_digits(arr, level):
    # Level can be used to adjust the difficulty
    for i in range(level):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        while arr[row][col] == 0:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
        arr[row][col] = 0

def generate_sudoku(level=40):
    arr = [[0 for _ in range(9)] for _ in range(9)]
    fill_diagonal(arr)
    fill_remaining(arr, 0, 3)
    remove_digits(arr, level)
    return arr

# Generate a Sudoku puzzle
print(generate_sudoku(40))  # The number here represents the difficulty level
