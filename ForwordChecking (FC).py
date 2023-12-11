import time
from Puzzles import Puzzles
 

def is_Valid(board, row, col, num):  #This function checks if placing the number num in the specified row and col of the Sudoku board (board) is consistent with the Sudoku rules.
    # Check if the number is already present in the row
    for i in range(9):  #It checks if num is not already present in the same row, the same column, or the same 3x3 subgrid.
        if board[row][i] == num:
            return False  # It returns "True" if the move is consistent (Valid) with the rules and "False" otherwise.

    # Check if the number is already present in the column
    for i in range(9):
        if board[i][col] == num:
            return False # It returns "True" if the move is consistent (Valid) with the rules and "False" otherwise.

    # Check if the number is already present in the 3x3 subgrid
    row1 = (row // 3) * 3
    col1 = (col // 3) * 3
    for i in range(row1, row1 + 3):
        for j in range(col1, col1 + 3):
            if board[i][j] == num:
                return False # It returns "True" if the move is consistent (Valid) with the rules and "False" otherwise.


    return True # It returns "True" if the move is consistent (Valid) with the rules and "False" otherwise.


def forward_checking(board, row, col, num): #This function performs forward checking to determine if the assignment of num to the cell (row, col) does not conflict with any future assignments.

    # Check if the number conflicts with any future assignments in the "same row"
    for i in range(col + 1, 9):
        if board[row][i] == num:
            return False #If a conflict is found, it returns False, indicating that the assignment is not valid; otherwise, it returns True.

    # Check if the number conflicts with any future assignments in the "same column"
    for i in range(row + 1, 9):
        if board[i][col] == num:
            return False #If a conflict is found, it returns False, indicating that the assignment is not valid; otherwise, it returns True.

    # Check if the number conflicts with any future assignments in the "same 3x3 subgrid"
    row1 = (row // 3) * 3
    col1 = (col // 3) * 3
    for i in range(row1, row1 + 3):
        for j in range(col1, col1 + 3):
            if i > row or (i == row and j > col):
                if board[i][j] == num:
                    return False #If a conflict is found, it returns False, indicating that the assignment is not valid; otherwise, it returns True.
    return True #no conflict > the assignment is valid 


def Unassigned_location(board): #This function searches for an unassigned (empty) cell in the Sudoku board.
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0: #Is empty?
                return row, col # It iterates through the entire board and returns the row and column indices of the first empty cell it encounters
    return None # If no empty cells are found, it returns None.


def solve_sudoku(board): #This is the main function that attempts to solve the Sudoku puzzle.
    #It first tries to find an unassigned cell using the *Unassigned_location* function.
    unassigned = Unassigned_location(board)

    #If all cells are assigned (no unassigned cells remain), the Sudoku puzzle is considered solved!, and it returns "True"
    if unassigned is None:
        return True #No unassigned cells 
    
    row, col = unassigned 

    # If there are unassigned cells, it iterates through the numbers from 1 to 9 and checks if each number is consistent(valid) with the rules using *is_Valid* and if it passes forward checking using *forward_checking*
    for num in range(1, 10):
        if is_Valid(board, row, col, num) and forward_checking(board, row, col, num):
           
            #If a number is consistent and doesn't lead to conflicts, it assigns the number to the cell.
            board[row][col] = num

            # Recursively solve the Sudoku puzzle with the updated board 
            if solve_sudoku(board):
                return True #If the recursive call leads to a solution, it returns True.

            # If the recursive call does not lead to a solution,
            # backtrack by resetting the cell to 0
            board[row][col] = 0

    # If no number can be assigned, the Sudoku puzzle has no solution
    return False



start_time=time.time()
if solve_sudoku(Puzzles.P99):# takes a puzzle from class Puzzles
    print("Solution:")
    for row in Puzzles.P99:
        print(row)#If a solution is found, it prints the solved Sudoku grid.
else:
    print("No Solution Exists for the given Sudoku board, Try Again with another board ") 



print("Execution Time: {:.4f} seconds".format(time.time()-start_time))