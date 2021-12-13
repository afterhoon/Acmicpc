## 플러그
## https://www.acmicpc.net/problem/2010

n = int(input())
plug = []
for _ in range(n):
    plug.append(int(input()))

print(sum(plug) - (len(plug) - 1)) # 꽂을 수 있는 플러그의 수는 모든 소켓수 - (멀티탭의 개수 - 1) 이다