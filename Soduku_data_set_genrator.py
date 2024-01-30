import csv
import os
from Soduku_genrator import generate_sudoku
from Soduku_solver_csp import solve_sudoku


# Function to convert Sudoku grid to a single string
def sudoku_to_string(sudoku):
    return ';'.join(','.join(str(cell) for cell in row) for row in sudoku)

# Main function to generate dataset
def generate_dataset(num_puzzles, difficulty_level):
    dataset = []
    for _ in range(num_puzzles):
        unsolved_puzzle = generate_sudoku(difficulty_level)
        solved_puzzle = [row[:] for row in unsolved_puzzle]  # Make a copy of the puzzle
        solve_sudoku(solved_puzzle)
        dataset.append([sudoku_to_string(unsolved_puzzle), sudoku_to_string(solved_puzzle)])

    return dataset

# Create 'source' directory if it doesn't exist
if not os.path.exists('data'):
    os.makedirs('data')

csv_file_path = os.path.join('data', 'sudoku_dataset.csv')
# Generate the dataset


difficulty = 40
size = 1000000
sudoku_dataset = generate_dataset(size, difficulty)  # 100 puzzles, adjust difficulty as needed

# Write dataset to CSV
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Unsolved', 'Solved'])
    writer.writerows(sudoku_dataset)

print("Dataset generated and saved as sudoku_dataset.csv")
