# 큐
# 큐를 구현하고 명령에 따른 처리

import sys
input = sys.stdin.readline

n = int(input())
order = [list(input().split()) for _ in range(n)]
queue = []

for i in range(n):
    if order[i][0] == 'push':
        queue.append(order[i][1])
    elif order[i][0] == 'pop':
        if not queue:
            print(-1)
        else:
            print(queue[0])
            queue = queue[1:]
    elif order[i][0] == 'size':
        print(len(queue))
    elif order[i][0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    elif order[i][0] == 'front':
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif order[i][0] == 'back':
        if not queue:
            print(-1)
        else:
            print(queue[-1])
