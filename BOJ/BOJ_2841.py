# 외계인의 기타 연주

import sys
input = sys.stdin.readline

# 입력 받기
n, p = map(int, input().split())
sound = [list(map(int, input().split())) for _ in range(n)]
# list(map()) 사용하는 이유
# map을 사용해서 모든 원소를 int형으로 바꿔준다
# map을 사용하면 map 객체가 return 되므로, 앞에 있는 값을 보려면 list로 변환해서 저장해야 함

stack = [[] for _ in range(7)] # 6개의 줄을 저장할 스택 선언
count = 0

for line, fret in sound: # 각 음의 줄 , 플랫 저장
    # for line, fret in sound: 2차원 배열의 값을 행 단위로 변수를 통해 접근 가능
    # 현재 첫번째 값의 line:2, fret:8

    # 비어있는 경우
    if len(stack[line]) == 0:
        stack[line].append(fret)
        count += 1

    # 비어있지 않은 경우
    else:
        if fret > stack[line][-1]:
            stack[line].append(fret)
            count += 1
        elif fret == stack[line][-1]:
            continue
        else:
            while len(stack[line]) != 0 and fret < stack[line][-1]:
                stack[line].pop()
                count += 1
            if len(stack[line]) != 0 and fret == stack[line][-1]: # 지금 연주되고 있다는 의미
                continue
            stack[line].append(fret)
            count += 1

print(count)


# 스택에서는 비어있는 경우를 고려해주어야 한다 !