board1 = [
  [7,8,0,4,0,0,1,2,0],
  [6,0,0,0,7,5,0,0,9],
  [0,0,0,6,0,1,0,7,8],
  [0,0,7,0,4,0,2,6,0],
  [0,0,1,0,5,0,9,3,0],
  [9,0,4,0,6,0,0,0,5],
  [0,7,0,3,0,0,0,1,2],
  [1,2,0,0,0,7,4,0,0],
  [0,4,9,2,0,6,0,0,7]
]

board2 = [
  [2,7,0,0,0,0,0,0,8],
  [8,4,0,3,1,0,9,0,0],
  [0,0,1,8,0,0,0,0,0],
  [0,0,0,0,0,4,0,0,2],
  [0,8,2,0,0,0,6,7,0],
  [5,0,0,2,0,0,0,0,0],
  [0,0,0,0,0,9,1,0,0],
  [0,0,5,0,4,8,0,9,6],
  [9,0,0,0,0,0,0,4,3]
]

board3 = [
  [2,6,0,0,1,5,0,7,0],
  [0,8,0,0,6,0,0,0,0],
  [0,0,0,0,0,8,5,6,0],
  [6,9,0,0,0,7,0,0,2],
  [8,1,0,0,0,0,0,0,0],
  [0,0,7,0,8,4,0,0,0],
  [0,0,0,0,0,0,0,5,0],
  [0,0,5,0,0,2,9,0,4],
  [7,0,0,0,0,0,0,0,0]
]


def solve(board):
  if not findEmpty(board):
    return True
  else:
    row, col = findEmpty(board)
  
  for num in range(1, 10):
    if isValid(board, num, (row, col)):
      printBoard(board)
      sleep(0.05)
      os.system("clear") 
      board[row][col] = num
      if solve(board):
        return True
      board[row][col] = 0
  return False


def isValid(board, num, pos):
  for i in range(len(board[0])):
    if board[pos[0]][i] == num and pos[1] != i:
      return False
  for i in range(len(board)):
    if board[i][pos[1]] == num and pos[0] != i:
      return False
  
  row = pos[0] // 3
  col = pos[1] // 3

  for i in range(row*3, row*3+3):
    for j in range(col*3, col*3+3):
      if board[i][j] == num and (i, j) != pos:
        return False
  return True


def printBoard(board):
  for row in range(len(board)):
    if row % 3 == 0 and row != 0:
      print("---------------------")
    for col in range(len(board[0])):
      if col % 3 == 0 and col != 0:
        print("| ", end="")
      if col == 8:
        print(board[row][col])
      else:
        print(str(board[row][col]) + " ", end="")


def findEmpty(board):
  for row in range(len(board)):
    for col in range(len(board[0])):
      if board[row][col] == 0:
        return (row, col)
  return None


import os
from time import sleep

# Menu
print("Sudoku Solver")
print("1: Easy")
print("2: Middle")
print("3. Hard")
select = input("Select a pattern you would like to play: ")

if select == str(1):
  solve(board1)
  printBoard(board1)
elif select == str(2):
  solve(board2)
  printBoard(board2)
elif select == str(3):
  solve(board3)
  printBoard(board3)
