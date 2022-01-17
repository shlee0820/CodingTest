# 쇠막대기

import sys
input = sys.stdin.readline

bracket = list(input())

stack = []
count = 0

for i in range(len(bracket)):
    if bracket[i] == '(':
        stack.append(bracket[i])

    else: # ) 인 경우
       if bracket[i-1] == '(':
           stack.pop()
           count += len(stack) # 스택에 있는 ( 개수 = 막대 갯수
       else:
           stack.pop()
           count += 1

print(count)
