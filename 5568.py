## 카드 놓기
## https://www.acmicpc.net/problem/5568

from itertools import permutations

n = int(input())
k = int(input())
card = []
for _ in range(n):
    card.append(input())

per = list(permutations(card, k)) # 순열 생성
res = []
for i in range(len(per)):
    temp = ""
    for j in range(k):
        temp += per[i][j]
    res.append(temp) # 각 순열을 한줄의 string으로 변환해 res에 입력
res = list(set(res)) # set을 거쳐 중복을 제거
print(len(res)) # 중복이 제거된 리스트의 길이를 구한다