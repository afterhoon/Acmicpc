## 카드 역배치
## https://www.acmicpc.net/problem/10804

from collections import deque

card = [i for i in range(21)]
temp = deque()

for _ in range(10):
    a, b = map(int, input().split())
    # 해당 구간의 부분수열을 temp 데크로 복사하여 역배열로 바꿔준다
    for i in range(a, b+1):
        temp.append(card[i])
    temp.reverse()

    # 바꿔준 temp를 다시 card의 해당위치에 덮어써준다
    for i in range(a, b+1):
        card[i] = temp.popleft()
print(" ".join(map(str, card[1:21])))