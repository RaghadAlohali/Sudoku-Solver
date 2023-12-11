import time # import time to measure the exectioun time for the functions
from Puzzles import Puzzles  # import class Puzzles that contains 20 sudoku puzzle

def checkConstraints(board, row, col, num): # constraints for suduko puzzle
    for i in range(9):  # this method checks the row and column for duplicate numbers
        if board[row][i] == num or board[i][col] == num:
            return False # it is against the constraints
        
    rowGrid = (row//3)*3  # this tells us which 3x3 grid do 'row' exist in
    colGrid = (col//3)*3  # this tells us which 3x3 grid do 'col' exist in
    for i in range(3):  # loop through the 3x3 grid
        for j in range(3):
            if board[rowGrid + i][colGrid + j] == num:  # checks the row and column for duplicate numbers
                return False # it is against the constraints

    return True  # number is valid in the current row, column, and grid = all constraints are satisifed  

def backtrack_sudoku(puzzle): # create the backtrack function that will take a sudoku puzzle
    for row in range(9):  # loop through each row of the sudoku board
        for col in range(9):  # loop through each column of the sudoku board
            if puzzle[row][col] == 0:  # check if the current cell is empty (if 0 it means it is empty)
                for num in range(1, 10):  # try numbers starting from 1 to 9
                    if checkConstraints(puzzle, row, col, num):  #check constraints for each cell
                        puzzle[row][col] = num  # assign number (num) to cell

                        if backtrack_sudoku(puzzle):  # call backtrack method (itself) to go through each row, col and check for constraints for each one
                            return True  # if the sudoku is solved return True (all full and true)
                        puzzle[row][col] = 0  # if not solved, backtrack by setting the cell back to 0 
                return False  # if no valid number can be placed, backtrack to the previous cell

    return True  # if all cells are filled, the Sudoku is solved




start_timeBT = time.time() # start measuring time

if backtrack_sudoku(Puzzles.p12): # takes a puzzle from class Puzzles
    for row in Puzzles.p12:
        print(row)         
        

end_timeBT = time.time() # stop measuring time

execution_timeBT = end_timeBT - start_timeBT # calculate the execution time
print("Execution time for BT: {:.4f}".format(execution_timeBT))