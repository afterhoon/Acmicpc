## 날짜 계산
## https://www.acmicpc.net/problem/1476

e, s, m = map(int, input().split())
x, y, z = 1, 1, 1
cnt = 1
while True:
    if e == x and s == y and m == z:
        break

    # 1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19
    x = x % 15 + 1
    y = y % 28 + 1
    z = z % 19 + 1
    
    cnt += 1

print(cnt)