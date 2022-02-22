# dfs
# 문제 : 유기농 배추

import sys
# 재귀호출 깊이 100만으로 설정
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, y):
    # if x <= -1 or x >= n or y <= -1 or y >= n:
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    if land[x][y] == 1:
        land[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True
    return False

t = int(input())

for _ in range(t):
    # 가로, 세로, 배추 갯수
    m, n, k = map(int, input().split())
    land = [[0] * m for _ in range(n)]

    for _ in range(k):
        M, N = map(int, input().split())
        land[N][M] = 1

    #print(*land)
    cnt = 0
    for i in range(n): # 세로/행
        for j in range(m): # 가로/열
            if dfs(i, j):
                cnt += 1

    print(cnt)
