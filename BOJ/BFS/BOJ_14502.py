# bfs
# 문제 : 연구소

# 리스트의 복사를 위한 모듈
import copy
from collections import deque
# 하나의 리스트에서 모든 조합을 구하기 위해 필요한 모듈
from itertools import combinations

import sys
input = sys.stdin.readline

# 각각 연구실 지도, 공백과 바이러스의 좌표값 저장 리스트
lab = []
blank = []
virus = []

# 세로, 가로 입력
n, m = map(int, input().split())

# 세로
for i in range(n):
    lab.append(list(map(int, input().split())))
    # 가로
    for j in range(m):
        # 공백인 경우
        if lab[i][j] == 0:
            blank.append((i, j))
        # 바이러스인 경우
        elif lab[i][j] == 2:
            virus.append((i,j))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# bfs 함수 정의
def bfs():
    copy_lab = copy.deepcopy(lab)
    # 바이러스가 있는 위치 좌표를 모두 큐에 넣음
    vq = deque(virus)
    # bfs
    while vq:
        x,y = vq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx <= n-1 and 0 <= ny <= m-1:
                # 감염 되지 않았다면
                if copy_lab[nx][ny] == 0:
                    # 감염시키기
                    copy_lab[nx][ny] = 2
                    vq.append((nx, ny))

    # 바이러스 감염 후 공백의 갯수 세기
    b_cnt = 0
    for i in range(n):
        for j in range(m):
            if copy_lab[i][j] == 0:
                b_cnt += 1

    return b_cnt


# 1. 3개의 조합 뽑기
b_cnt = 0
for w_pos in combinations(blank, 3):
    for x,y in w_pos:
        # 벽 설치 고고
        lab[x][y] = 1
    # 2. bfs 탐색 후, 공백의 갯수의 최댓값 구하기
    b_cnt = max(b_cnt, bfs())
    # 3. 벽 허물고 다시 도전
    for x,y in w_pos:
        lab[x][y] = 0

print(b_cnt)