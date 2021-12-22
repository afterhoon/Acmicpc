## 홀수
## https://www.acmicpc.net/problem/2576

sum = 0
lownum = 100
for i in range(7):
    n = int(input())
    if n % 2 == 1:
        sum += n # 홀수일 경우를 모두 더함
        if lownum > n:
            lownum = n # 최소값보다 작으면 해당 값을 최소값으로 설정
if sum == 0: # 합계가 없으면 홀수가 없는 것이므로 -1을 출력하고 종료
    print("-1")
else:
    print(sum)
    print(lownum)