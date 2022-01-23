# A -> B
# 문제 : 연산 두 가지를 활용 하여 A->B로 만드는 최소 연산 횟수 구하기

import sys
input = sys.stdin.readline
a, b = map(int, input().split())
cnt = 0

# a=100, b=40021
while 1:
    if a == b:
        break
    elif a > b or (b % 2 != 0 and b % 10 != 1):
        break
    elif b % 2 == 0: # 2로 나눌 수 있으면, 나누기
        b = b // 2
        cnt += 1
    elif b % 10 == 1: # 끝 자리가 1이면, 1의 자리 없애기
        b = b // 10
        cnt += 1

if a == b:
    print(cnt+1)
else:
    print(-1)