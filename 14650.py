## 걷다보니 신천역 삼 (Small)
## https://www.acmicpc.net/problem/14650

n = int(input())
ans = 0
 
def func(k, sum):
    global ans
    for i in range(3):
        if k == 0 and i == 0:
            continue
        if k == n:
            if sum % 3 == 0:
                ans += 1
                return ans
        else:
            func(k + 1, sum + i)
 
func(0, 0)
print(ans)