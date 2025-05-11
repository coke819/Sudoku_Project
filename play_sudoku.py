import random
from generate_sudoku import generate_sudoku
from print_board import print_board

def play_sudoku():
	solution = generate_sudoku()
	puzzle = [row[:] for row in solution]
    empties = [(r, c) for r in range(9) for c in range(9)]
    for _ in range(40):
        r, c = random.choice(empties)
        empties.remove((r, c))
        puzzle[r][c] = 0

    board = puzzle
    while True:
        print_board(board)
        if all(all(val != 0 for val in row) for row in board):
            print("🎉 축하합니다! 퍼즐을 완성하셨습니다.")
            break

        move = input("입력 → row col num (1-9, 공백 구분, 종료=q): ")
        if move.lower() == 'q':
            print("게임을 종료합니다.")
            break

        try:
            row, col, num = map(int, move.split())
            if not (1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9):
                print("❌ 1에서 9 사이의 숫자를 입력하세요.")
                continue
            row -= 1; col -= 1

            # 정답과 비교
            if solution[row][col] != num:
                print("❌ 잘못된 이동입니다. 게임 오버!")
                break
            if board[row][col] != 0:
                print("⚠️ 이미 채워진 칸입니다.")
                continue

            board[row][col] = num

        except ValueError:
            print("❌ 입력 형식을 확인하세요. 예) 3 5 9")
