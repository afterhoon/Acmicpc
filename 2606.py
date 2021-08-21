## 웜 바이러스
## https://www.acmicpc.net/problem/2606

# 그래프 전체를 탐색하기 위해 dfs 알고리즘을 이용한다
# 입력한 번호와 연결된 모든 위치를 체크한다
def dfs(x):
    for i in dic[x]:
        if i not in visited:
            visited.append(i)
            dfs(i)

n = int(input())
line = int(input())
dic = {}
visited = []

# 각 번호에 인접한 번호를 모두 입력한다
for i in range(n):
    dic[i+1] = set()
for i in range(line):
    a, b = map(int, input().split())
    dic[a].add(b)
    dic[b].add(a)

dfs(1)
print(len(visited)-1)   # visited에는 자기 자신도 포함되어 있으므로 1을 빼준다