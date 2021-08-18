## 거스름돈
## https://www.acmicpc.net/problem/5585

coin = [500, 100, 50, 10, 5, 1]
price = 1000 - int(input())
cnt = 0

# 비싼 동전부터 차례로 가능한 많이 지불해준다
# 지불해줄때마다 cnt를 +1 해준다
for c in coin:
    while price >= c:
        price -= c
        cnt += 1

print(cnt)