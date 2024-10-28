def is_valid(board, row, col, num):
    # 해당 숫자가 같은 행에 있는지 확인
    if num in board[row]:
        return False
    # 해당 숫자가 같은 열에 있는지 확인
    if num in [board[i][col] for i in range(9)]:
        return False
    # 해당 숫자가 같은 3x3 박스에 있는지 확인
    start_row, start_col = 3 * (row // 3), 3 * (col // 3) # // 몫의 값을 나타낸다. -> 내가 포함된 3x3박스의 좌측 상단 시작점!
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
    # 빈값, 아직 안 푼 곳을 찾고
    empty_loc = find_empty_location(board)
    if not empty_loc: # not None = True
        return True  # 모든 빈칸을 다 채운 경우, 끝
    
    # 빈 위치
    row, col = empty_loc

    for num in range(1, 10): # 빈값에 1~9를 다 넣어보면서, 유효한 값을 찾는다.
        if is_valid(board, row, col, num):
            board[row][col] = num # 유효하면, 대입!

            # 위 규칙에 의거, 값을 채워 넣었는데, 결국 스도쿠를 해결하지 못했다면,
            if solve_sudoku(board):
                return True

            board[row][col] = 0  # 실패한 경우, 백트래킹

    return False  # 이 경로로는 해결 불가

# 주어진 스도쿠 퍼즐을 해결하는 함수 호출
board = [
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

print("초기 스도쿠 퍼즐:")
print_board(board)
print("\n해결된 스도쿠 퍼즐:")

if solve_sudoku(board):
    print_board(board)
else:
    print("해결할 수 없는 스도쿠 퍼즐입니다.")