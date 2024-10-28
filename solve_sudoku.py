def is_valid(board, row, col, num):
    # 행에 num이 있는지 확인
    if num in board[row]:
        return False
    # 열에 num이 있는지 확인
    if num in [board[i][col] for i in range(9)]:
        return False
    # 3x3 박스에 num이 있는지 확인
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False
    return True

def find_empty_location(board):
    # 비어 있는 위치(0)를 찾음
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None

def solve_sudoku(board):
    # 스도쿠 퍼즐을 해결
    empty_loc = find_empty_location(board)
    if not empty_loc:
        return True

    row, col = empty_loc
    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # 백트래킹
    return False