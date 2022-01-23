# 치킨 TOP N
# 문제 설명 : 치킨 집의 맛의 수치를 감소 하지 않는(증가 및 동일) 순으로 정렬

n = int(input())
input_list = list(map(int, input().split()))
k = int(input())

temp_list = []
size = n//k # 1명 당 정렬 해야 하는 배열의 크기
for i in range(0, n, size):
    temp_list += sorted(input_list[i:i+size])
print(" ".join(str(i) for i in temp_list))
print(*temp_list)
