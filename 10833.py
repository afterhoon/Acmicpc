## 사과
## https://www.acmicpc.net/problem/10833

n = int(input())
ans = 0
for i in range(n):
    stu, apple = map(int, input().split())
    ans += apple % stu # 나눠지지 않는 나머지를 더해준다
print(ans)