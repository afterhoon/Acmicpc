## 가장 긴 증가하는 부분 수열 3
## https://www.acmicpc.net/problem/12738
# x 시간초과

n = int(input())
a = list(map(int, input().split()))
ans = 0
def func(index, num, cnt):
    global ans
    if index == n:
        ans = max(ans, cnt)
        return
    
    for i in range(index, n):
        if num < a[i]:
            func(i+1, a[i], cnt+1)

func(0, -1000000001, 0)
print(ans)