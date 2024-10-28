from generate_sudoku import generate_sudoku
from print_board import print_board
from solve_sudoku import is_valid, find_empty_location

def play_sudoku():
    board = generate_sudoku()
    print("스도쿠 게임을 시작합니다!")
    print_board(board)

    while True:
        try:
            row = int(input("행을 입력하세요 (1-9): ")) - 1
            col = int(input("열을 입력하세요 (1-9): ")) - 1
            num = int(input("숫자를 입력하세요 (1-9): "))

            if not (0 <= row <= 8 and 0 <= col <= 8 and 1 <= num <= 9):
                print("잘못된 입력입니다. 1에서 9 사이의 숫자를 입력하세요.")
                continue

            if board[row][col] != 0:
                print("이미 값이 입력된 칸입니다.")
                continue

            if is_valid(board, row, col, num):
                board[row][col] = num
                print_board(board)

                if not find_empty_location(board):
                    print("축하합니다! 스도쿠를 완성했습니다.")
                    break
            else:
                print("잘못된 이동입니다. 다시 시도하세요.")
        except ValueError:
            print("잘못된 입력입니다. 숫자를 입력하세요.")

# 파일을 직접 실행할 때만 play_sudoku()를 실행
if __name__ == "__main__":
    play_sudoku()