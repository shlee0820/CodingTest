# dfs
# 문제 : 단지 번호 붙이기
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip('\n'))))

home_list = []
home = 0

def dfs(x, y):
    global home
    # 지도 범위 벗어나면 False 반환
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 만약 해당 노드에 집이 존재 하면
    if graph[x][y] == 1:
        # 단지 내 집의 갯수를 세는 변수
        home += 1
        # 1일때 count되므로 방문했음을 확인하도록 0으로 변경
        graph[x][y] = 0
        dfs(x - 1, y)
        dfs(x, y - 1)
        dfs(x + 1, y)
        dfs(x, y + 1)
        return True

for i in range(n):
    for j in range(n):
        if dfs(i, j):
            home_list.append(home)
            home = 0

print(len(home_list))
home_list.sort()
for i in home_list:
    print(i)