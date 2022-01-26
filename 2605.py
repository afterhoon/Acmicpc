## 줄 세우기
## https://www.acmicpc.net/problem/2605

n = int(input())
s = list(map(int, input().split()))
ans = []

for i in range(n):
    ans.insert(i-s[i], i+1) # 각 학생을 (학생의 번호 - 학생이 뽑은 숫자) 인 index에 넣어준다

print(" ".join(map(str, ans)))