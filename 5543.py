## 상근날드
## https://www.acmicpc.net/problem/5543

hamburger = 3000
drink = 3000
ans = 0
for _ in range(3):
    hamburger = min(hamburger, int(input()))
for _ in range(2):
    drink = min(drink, int(input()))
print(hamburger + drink - 50) # 햄버거와 음료의 최저가