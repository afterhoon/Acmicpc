## 영화감독 숌
## https://www.acmicpc.net/problem/1436

n = int(input())
cnt = 0
ans = 0
# 시간제한이 2초로 비교적 널널한 편이기 때문에 
# 해당 숫자가 나올때까지 순회하는 방법을 사용했다
while n > cnt:
    ans += 1
    if "666" in str(ans):
        cnt += 1

print(ans)