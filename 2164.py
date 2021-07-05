## 카드2
## https://www.acmicpc.net/problem/2164

from collections import deque

# 입력받은 수만큼의 카드를 deque로 생성한다
n = int(input())
dq = deque([(i+1) for i in range(n)])
cnt = 0

while True:
    cnt += 1
    temp = dq.popleft()

    # deque의 크기가 0이 되면 마지막 카드를 뽑은 것이므로 
    # 반복을 종료하고 마지막 숫자를 출력한다
    if len(dq) <= 0:
        break
    
    # 맨 윗장의 숫자를 temp에 기록한 뒤 
    # cnt가 홀수일 경우 그냥 버리고 짝수일 경우 맨 아래(deque의 맨 끝)로 옮긴다
    if cnt % 2 == 0:
        dq.append(temp)

print(temp)