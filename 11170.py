## 0의 개수
## https://www.acmicpc.net/problem/11170

t = int(input())

for _ in range(t):
    cnt = 0
    n, m = map(int, input().split())
    for i in range(n,m+1):
        # 숫자를 string으로 변환한 뒤 0의 개수를 카운트한다
        cnt += str(i).count("0")
    print(cnt)