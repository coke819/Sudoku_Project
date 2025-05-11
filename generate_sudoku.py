from initialize_board import initialize_board
from solve_sudoku import solve_sudoku

def generate_sudoku():
    board = initialize_board()
    solve_sudoku(board)
    return board