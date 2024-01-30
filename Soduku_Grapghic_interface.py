import tkinter as tk
from tkinter import messagebox
from Soduku_genrator import generate_sudoku
from Soduku_solver_csp import solve_sudoku

def on_entry_click(event, entry):
    """Function to clear the entry when clicked."""
    entry.delete(0, tk.END)

def validate_entry(P):
    """Function to validate entries to be only digits and of length 1."""
    return (P.isdigit() or P == "") and len(P) <= 1

def submit():
    """Function to get values from entries and perform an action."""
    try:
        grid_values = [[int(entries[row][col].get() or 0) for col in range(9)] for row in range(9)]
        # You can process grid_values here
        print(grid_values)  # Example action
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter only digits from 1 to 9.")
def populate_grid_with_puzzle(puzzle):
    """Populate the Tkinter grid with the puzzle values."""
    for row in range(9):
        for col in range(9):
            value = puzzle[row][col]
            if value != 0:
                entries[row][col].insert(0, value)
                entries[row][col]['state'] = 'readonly'  # Make the cell read-only
            else:
                entries[row][col].delete(0, tk.END)
                entries[row][col]['state'] = 'normal'
def solve_puzzle():
    """Solve the puzzle and update the GUI with the solution."""
    # Get the current state of the Sudoku grid
    current_puzzle = [[int(entries[row][col].get() or 0) for col in range(9)] for row in range(9)]

    # Solve the puzzle
    solved = solve_sudoku(current_puzzle)
    if solved:
        # Update the GUI with the solved puzzle
        populate_grid_with_puzzle(solved)
    else:
        messagebox.showinfo("Sudoku Solver", "No solution found for the current puzzle.")
# Create the main window
window = tk.Tk()
window.title("Sudoku")

# Create a grid of Entry widgets
entries = []
for row in range(9):
    row_entries = []
    for col in range(9):
        entry = tk.Entry(window, width=2, font=('Arial', 24), justify='center', validate="key")
        entry['validatecommand'] = (entry.register(validate_entry), '%P')
        entry.grid(row=row, column=col, sticky='nsew', padx=2, pady=2)
        entry.bind("<Button-1>", lambda event, e=entry: on_entry_click(event, e))
        row_entries.append(entry)
    entries.append(row_entries)

# Generate a new Sudoku puzzle and populate the grid
new_puzzle = generate_sudoku(40)  # Adjust the difficulty level as needed
populate_grid_with_puzzle(new_puzzle)

# Create a submit button
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.grid(row=9, column=0, columnspan=4)

# Create a solve button
solve_button = tk.Button(window, text="Solve", command=solve_puzzle)
solve_button.grid(row=9, column=5, columnspan=4)

# Run the application
window.mainloop()