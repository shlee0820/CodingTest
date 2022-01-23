# 신입 사원
# 최대 신입 사원 수 구하기

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    rank = [list(map(int, input().split())) for _ in range(n)]
    rank.sort(key=lambda x:x[0])

    m = rank[0][1]
    cnt = 1
    for i in range(1, n):
        if m > rank[i][1]: 
            cnt += 1
            m = rank[i][1]

    print(cnt)
