# 설탕 공장

# 봉지 : 3kg / 5kg
# 봉지 최소 갯수 구하기

n = int(input())
count = 0

while n >= 0:
    if n % 5 == 0:
        count += n // 5
        print(count)
        break
    else:
        n -= 3
        count += 1
else: # while문 빠져나가면
    print(-1)
