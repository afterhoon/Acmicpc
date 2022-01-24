## 후위 표기식2
## https://www.acmicpc.net/problem/1935

import sys

n = int(input())
arr = input()
nums = []
for i in range(n):
    nums.append(int(input()))

stack = []
for c in arr:
    if c in ['+', '-', '*', '/']: # 연산자라면
        # 계산을 위해 num1과 num2를 빼낸다 (pop()은 뒤부터 빼내므로 num2가 먼저 나온다)
        num2 = stack.pop()
        num1 = stack.pop()
        # 각 연산자에 맞는 연산수행
        if c=='+':
            stack.append(num1+num2)
        elif c=='-':
            stack.append(num1-num2)
        elif c=='/':
            stack.append(num1/num2)
        elif c=='*':
            stack.append(num1*num2)
    else: # 숫자라면
        stack.append(nums[ord(c)-ord('A')]) # 문자를 값으로 치환해주고 stack에 저장

print(f"{stack.pop():.2f}")