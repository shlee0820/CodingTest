# 가장 큰 수
# 문제 : 리스트 안의 정수 들이 주어질 때, 이것 들을 이어 붙여 만들 수 있는 수들 중 가장 큰 수 만들기
# 아이디어
# 1. 사용자로 부터 입력을 받는다.
# 2. 각각의 원소들의 자릿수를 따져가며 정렬을 한다.
# 3. 가장 큰 수부터 정렬이 될 것이므로 그것들을 모두 이어붙인다.

# how to sort
# 입력받은 배열의 원소들의 각 자리수를 떼어놓기 위해 int->string->list
# 입력 가능한 수는 999까지 이므로 제일 앞자리부터 비교를 진행하여 정렬
# 0번 인덱스 내림차순, 1번 인덱스 내림차순, 2번 인덱스 내림차순

def solution(numbers):
    numbers = list(map(str, numbers))
    # x*3인 이유 :  numbers의 원소가 1자리수 일때, 최소 3자리로 만들고 싶어서
    numbers.sort(key=lambda x: x*3, reverse=True) # 내림차순 정렬
    # numbers(리스트)의 원소를 join을 통해 문자열로 합쳐줌 -> int로 변환 후 -> 문자열 변환
    return str(int(''.join(numbers))) # int -> str : 000과 같은 경우 0으로 출력하기 위해 필요

