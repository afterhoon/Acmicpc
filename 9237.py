## 이장님 초대
## https://www.acmicpc.net/problem/9237

n = int(input())
t = list(map(int, input().split()))

# 나무를 가장 단시간에 모두 자라게 하기 위해서는 오래걸리는 나무부터 심어야한다
# 따라서 내림차순으로 정렬해준다
t.sort(reverse=True)

# 각 나무는 심는데 하루가 걸리므로 i+1 씩 더해준다
for i in range(n):
    t[i] += i + 1

# 모든 나무가 자란 다음날 이장님을 초대하므로 가장 큰 일수에 +1을 해서 출력한다
print(max(t) + 1)