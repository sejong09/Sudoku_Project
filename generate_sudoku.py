import random
from initialize_board import initialize_board
from solve_sudoku import solve_sudoku

def generate_sudoku(difficulty=30):
    board = initialize_board()
    # 스도쿠 퍼즐을 무작위로 채우고 풀이
    solve_sudoku(board)
    
    # 난이도 조절을 위해 일부 숫자를 제거
    removed_cells = difficulty
    while removed_cells > 0:
        row, col = random.randint(0, 8), random.randint(0, 8)
        if board[row][col] != 0:
            board[row][col] = 0
            removed_cells -= 1
    return board