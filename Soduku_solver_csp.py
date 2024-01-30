from constraint import Problem, AllDifferentConstraint
import time
def solve_sudoku(puzzle):
    # Create a new constraint problem
    problem = Problem()

    # Define variables with domains
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == 0:  # If the place is empty
                problem.addVariable((row, col), range(1, 10))
            else:
                problem.addVariable((row, col), [puzzle[row][col]])

    # Add constraints for rows, columns, and squares
    for i in range(9):
        problem.addConstraint(AllDifferentConstraint(), [(i, j) for j in range(9)])  # Rows
        problem.addConstraint(AllDifferentConstraint(), [(j, i) for j in range(9)])  # Columns

    for row in range(0, 9, 3):
        for col in range(0, 9, 3):
            square = [(row + i, col + j) for i in range(3) for j in range(3)]
            problem.addConstraint(AllDifferentConstraint(), square)

    # Solve the problem
    solution = problem.getSolution()

    # If a solution exists, fill in the puzzle
    if solution:
        for row, col in solution.keys():
            puzzle[row][col] = solution[row, col]

    return puzzle

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
solved_puzzle = solve_sudoku(puzzle)
end_time = time.time()

# Print the solution
for row in solved_puzzle:
    print(" ".join(str(num) for num in row))

print(f"Sudoku solved in {end_time - start_time:.4f} seconds")