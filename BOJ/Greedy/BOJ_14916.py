# 거스름돈
# 문제 : 동전의 갯수가 최소가 되도록 거슬러 주어라

n = int(input())
cnt = 0

# 먼저 2를 빼고 난 후, 5의 배수 인지 확인
while n > 0:
    if n % 5 == 0:
        cnt += n // 5
        n = n % 5
        break
    else:
        n -= 2
        cnt += 1
if n != 0:
    print(-1)
else:
    print(cnt)
