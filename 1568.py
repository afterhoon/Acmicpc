## 새
## https://www.acmicpc.net/problem/1568

n = int(input())
cnt = 0
k = 0
# 새가 모두 날아갈 때까지 반복한다
while n > 0:
    k += 1      # 매번 음계(날아가는 새의 수)를 늘린다
    if n < k:   # 만약 남은 새의 수보다 날아갈 새의 수가 크다면 처음으로 되돌린다
        k = 0
        continue
    n -= k      # 날아간 수만큼 현재 새의 수를 차감
    cnt += 1    # 초를 1 늘려준다
print(cnt)