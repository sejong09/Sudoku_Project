# 9x9 보드. 리스트로 0 블럭만 생성, 0을 빈칸으로 생각
def initialize_board():
  return [[0] * 9 for _ in range(9)]