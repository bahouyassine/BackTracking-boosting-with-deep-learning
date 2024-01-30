import time

def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))

def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return -1, -1

def is_safe(board, row, col, num):
    # Check if 'num' is not in the given row
    if num in board[row]:
        return False

    # Check if 'num' is not in the given column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if 'num' is not in the given 3x3 box
    box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + box_start_row][j + box_start_col] == num:
                return False

    return True

def solve_sudoku(board):
    row, col = find_empty_location(board)

    # If no empty space is left, puzzle is solved
    if row == -1 and col == -1:
        return True

    for num in range(1, 10):
        if is_safe(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True

            # Backtrack
            board[row][col] = 0

    return False

# Example Sudoku Puzzle (0 represents an empty cell)

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

start_time = time.time()

if solve_sudoku(puzzle):
    end_time = time.time()
    print_board(puzzle)
    print(f"Sudoku solved in {end_time - start_time:.2f} seconds")
else:
    end_time = time.time()
    print("No solution exists")
    print(f"Execution time: {end_time - start_time:.2f} seconds")
