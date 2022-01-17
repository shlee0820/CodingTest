# 문제 주요 내용 : 덩치가 큰 순서대로 등수 매기기
# 입력조건 : 사람의 수(20이상 50이하), 키와 몸무게(10이상 200이하)
# 출력조건 : 등수를 숫자로 나열하여 출력하기

# 입력 받기
input_num = int(input())
people_info_list = []

for _ in range(input_num):
    weight, height = map(int, input().split()) #한꺼번에 int형으로 바꾸기
    people_info_list.append((weight, height))

for i in people_info_list:
    rank = 1
    for j in people_info_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
