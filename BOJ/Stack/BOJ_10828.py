# 스택
# 문제 : 스택 구현 후 명령 처리
# 명령 : push, pop, size, empty, top 

import sys

# 명령의 수 입력 받기
n = int(sys.stdin.readline())

# 스택 선언
stack = []

# 명령 입력 받기
for i in range(n):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])




