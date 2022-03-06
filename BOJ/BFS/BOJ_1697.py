# bfs
# 문제 : 숨바꼭질

import sys
input = sys.stdin.readline

from collections import deque


def bfs():
    q = deque()
    q.append(N)  # 시작 노드

    while q:
        x = q.popleft()
        if x == K:
            print(sec_cnt[x])
            break
        else:  # 동생과 만나지x
            for i in (x - 1, x + 1, x * 2):
                if 0 <= i <= MAX and not sec_cnt[i]:
                    sec_cnt[i] = sec_cnt[x] + 1
                    q.append(i)


MAX = 10 ** 5  # N,K의 최댓값
N, K = map(int, input().split())
sec_cnt = [0] * (MAX + 1)  # 해당 배열의 값은 해당 인덱스로 오기 까지의 연산 횟수(초)

bfs()
