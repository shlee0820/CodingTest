# 막대기
# 문제 : n개의 막대기가 있을 때, 오른쪽에서 봤을 때 보이는 막대기의 갯수 구하기

import sys
input = sys.stdin.readline

n = int(input())
height = [int(input()) for _ in range(n)]

t = height.pop()
count = 1
for _ in range(n-1):
    nt = height.pop()
    if t < nt:
        count += 1
        t = nt

print(count)