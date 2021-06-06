## 쇠막대기
## https://www.acmicpc.net/problem/10799

bar = list(input())
stack = []
stick = 0
for i in range(len(bar)):
    ## '(' 이 나오면 스택에 저장
    if bar[i] == '(':
        stack.append('(')
    ## ')'이 나오면 하나를 pop하고 바로 앞 원소가 '('라면 스택의 크기만큼 숫자를 증가하고 ')'라면 1을 증가시킨다
    else:
        stack.pop()
        if bar[i-1] == '(':
            stick += len(stack)
        else:
            stick += 1
print(stick)
