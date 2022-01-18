# 한수
# 문제 주요 내용 : 1이상이고, 입력받은 숫자이하인 한수의 갯수 구하기
# 출력조건 : 갯수를 출력

# 한수의 조건 : 각 자리가 등차수열을 이룬다
# 고려 사항 : 두 자리 이하 숫자는 모두 한수 취급

def hansu(input_num):
    # 1-입력값까지의 수를 생성하여 각자리수별로 리스트 만들기
    count, sub_1, sub_2 = 0, 0, 0
    for i in range(1, input_num + 1):
        # 100보다 작은수 -> 모두 한수로 count
        if i < 100:
            count += 1
        else:
            input_list = list(map(int, str(i)))
            sub_1 = input_list[0] - input_list[1]
            sub_2 = input_list[1] - input_list[2]
            if sub_1 == sub_2:
                count += 1
    return count

# 사용자에게 입력받기
input_num = int(input())

print(hansu(input_num))
