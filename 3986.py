## 좋은 단어
## https://www.acmicpc.net/problem/3986

n = int(input())
cnt = 0
for _ in range(n):
    s = list(input())
    stack = []

    for i in range(len(s)):
        # 스택의 마지막 원소가 커서 위치의 문자와 같다면 제거
        # 단 최초에 stack이 비어있으므로 반드시 추가시켜줘야함
        if stack and stack[-1] == s[i]: 
            stack.pop()
        # 같지 않다면 추가
        else:
            stack.append(s[i])

    # 스택이 비어있다면 모든 쌍을 찾은 것이므로 카운트 1증가
    if not stack:
        cnt += 1

print(cnt)