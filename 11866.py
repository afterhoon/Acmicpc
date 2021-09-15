## 요세푸스 문제 0
## https://www.acmicpc.net/problem/11866

n, k = map(int, input().split())
table = [i for i in range(1,n+1)]
visit = [False for i in range(1, n+1)]
ans = []
cnt = 0
i = -1
len = 0

# 모든 사람을 방문할때까지 순회
while len < n:
    i = (i + 1) % n

    # 방문한 사람이면 건너뛴다
    if visit[i]:
        continue

    cnt = (cnt + 1) % k # 매 k번째 사람을 방문
    if cnt == 0:        # 방문하면 visit을 True로 변경하고 ans에 추가
        visit[i] = True
        ans.append(table[i])
        len += 1

print("<", ", ".join(map(str, ans)), ">", sep="")