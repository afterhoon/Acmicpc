## 완전수
## https://www.acmicpc.net/problem/14563

t = int(input())
arr = map(int, input().split())
for n in arr:
    res = 0
    for i in range(1, n-1):
        # 약수이면 res에 모두 합해줌 (본인숫자는 제외)
        if n % i == 0:
            res += i
    if res == n:
        print("Perfect")
    elif res < n:
        print("Deficient")
    else:
        print("Abundant")
