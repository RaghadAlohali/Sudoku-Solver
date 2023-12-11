import time
from Puzzles import Puzzles

# We first need a function to check if a choice is accepted, if putting number in the cell (row,col) doesn't break the condition
def is_acccepted(board, row, col, num):
    for i in range(9):
        #check if (number) is not in (row , col , 3*3 square)
        if board[row][i] == num or board[i][col] == num or board[row - row % 3 + i // 3][col - col % 3 + i % 3] == num:
            return False
    return True


def calculate_cell_domain(board, row, col):
    domain = set(range(1, 10))
    
    # Check values in the same row
    for value in board[row]:
        if value in domain:
            domain.remove(value)
    
    # Check values in the same column
    for i in range(9):
        value = board[i][col]
        if value in domain:
            domain.remove(value)
    
    # Check values in the same 3x3 box
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            value = board[i][j]
            if value in domain:
                domain.remove(value)

    return domain

def empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None


# Function to perform MAC propagation
def mac_propagation(board):
    while True:
        updated = False
        for i in range(9):
            for j in range(9):
                # Skip cells that are already filled
                if board[i][j] != 0:
                    continue
                # Get the domain of possible values for the current cell
                domain = calculate_cell_domain(board, i, j)
                if len(domain) == 1:
                     # Assign the single value to the current cell
                    board[i][j] = domain.pop()
                    updated = True
        # If no more updates are made, exit the loop
        if not updated:
            break

# MAC algorithm to solve the Sudoku puzzle
def mac_sudoku(board):
    # Find an empty cell
    cell = empty_cell(board)
    if cell is None:
        return True  #the puzzle is solved

    row, col = cell
    domain = calculate_cell_domain(board, row,col) # Try different numbers from the domain of the cell
    # Try values from the domain
    for num in domain:
        board[row][col] = num
        # Create a copy of the board for recursive call
        new_board = [row[:] for row in board]
        # Perform MAC propagation on the new board
        mac_propagation(new_board)
        # Recursive call to solve the remaining puzzle
        if mac_sudoku(new_board):
            # Copy the solved board back to the original board
            for i in range(9):
                for j in range(9):
                    board[i][j] = new_board[i][j]
            return True

    # If no valid number is found, the puzzle is unsolvable
    return False




start_time = time.time()
if mac_sudoku(Puzzles.p12):# takes a puzzle from class Puzzles
   print("Solution:")
   for row in Puzzles.p12:
        print(row)
else:
     print("No solution exists.")

print("Execution Time: {:.4f} seconds".format(time.time()-start_time))

