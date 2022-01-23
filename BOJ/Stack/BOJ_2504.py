# 괄호의 값
# 문제 : 괄호열에 맞는 결과값 출력하기

import sys
input = sys.stdin.readline

str = list(input()) # (()[[]])
stack = []

for s in str:
    val = 0
    if s == '(' or s == '[':
        stack.append(s)
    else: # ) or ] 인 경우, 현재 stack에는 ( ( 저장되있음
        if s == ')':
            if not stack or p == '[':  # 올바르지 않은 괄호열
                print(0)
                sys.exit(0)
            while stack:
                p = stack.pop()  # (
                if p == '(':
                    if val == 0:
                        stack.append(2)
                    else:
                        stack.append(val*2)
                else:  # ) or ]
                    val += p



        elif s == ']':
            while stack:
                if not stack or p == '()':  # 스택이 비어있을 때
                    print(0)
                    sys.exit(0)






