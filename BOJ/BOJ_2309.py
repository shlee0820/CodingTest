# 일곱 난쟁이
# 문제 주요 내용 : 9개의 숫자가 주어졌을 때, 그 중 7개의 합이 100이되는 조합을 찾는 문제
# 출력조건 : 오름차순

# 입력숫자 설정
input_num = 9

# 9번의 입력 받기
input_list = [int(input()) for i in range(input_num)]

sum_value = sum(input_list)
temp_1, temp_2 = 0, 0

# 브루트포스 알고리즘
# 이중포문을 활용하여 전체적으로 검사 진행, 전체 입력값의 합에서 2가지 원소를 제거한 값이 100일때 temp1,temp2에 두개의 값 저장
for i in range(input_num):
    for j in range(i+1, input_num):
        if (sum_value - (input_list[i] + input_list[j])) == 100:
            temp_1 = input_list[i]
            temp_2 = input_list[j]

# 두개의 원소 삭제
input_list.remove(temp_1)
input_list.remove(temp_2)

# 정렬하여 출력
print(' '.join(map(str, sorted(input_list))))

# 전체적인 과정
# 1. 숫자를 9개 입력받기
# 2. 입력받은 숫자를 리스트로 받아, 이중포문을 통해 2개의 요소를 검사
# 3. 만약, 전체의 합에서 두가지 요소를 뺀 값이 100일때 두개의 값을 삭제