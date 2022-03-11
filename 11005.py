## 진법 교환 2
## https://www.acmicpc.net/problem/11005

notation = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
n, b = map(int, input().split())
ans = ''

while n != 0:
    ans += str(notation[n % b])
    n = n // b

print(ans[::-1])