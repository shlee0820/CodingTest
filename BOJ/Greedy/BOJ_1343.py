# 폴리오미노
# 문제 : .와 x로 이루어진 보드판을 AAAA,BB로 채우기

import sys
input = sys.stdin.readline

board = input().rstrip("\n")
idx = 0

while len(board) > idx:
   if board[idx] == '.':
       idx += 1
   elif board[idx:idx+4] == 'XXXX':
       board = board.replace('XXXX', 'AAAA', 1)
       idx += 4
   elif board[idx:idx+2] == 'XX':
       board = board.replace('XX', 'BB', 1)
       idx += 2
   else:
       idx = -1
       break
if idx == -1:
    print(-1)
else:
    print(board)
