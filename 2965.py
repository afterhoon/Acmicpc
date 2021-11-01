## 캥거루
## https://www.acmicpc.net/problem/2965

a, b, c = map(int, input().split())

#캥거루가 뛸때 항상 다른 캥거루에 인접한곳으로 뛰면 최대치가 나온다
#따라서 첫 a-b와 b-c 중 큰쪽의 차이만큼이 최대치 이다
print(max(b-a, c-b)-1)