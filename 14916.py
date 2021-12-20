## 거스름돈
## https://www.acmicpc.net/problem/14916

n = int(input())
balance = n % 5
cnt = n // 5

if n == 1 or n == 3: # 거슬러줄 수 없는 경우
    print("-1")
elif balance % 2 == 0: # 5원을 최대로 챙긴 뒤 2원으로 나누어 떨어지는 경우
    print(cnt + balance//2)
else: # 2원으로 나누어떨어지지 않는 경우 5원을 하나 빼면 짝수의 거스름돈이 남으므로 2원짜리로 거스름돈을 받을수 있음
    print(cnt-1 + (balance+5)//2)