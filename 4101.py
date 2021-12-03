## 크냐?
## https://www.acmicpc.net/problem/4101

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print("YES" if a > b else "NO") #a가 b보다 클때만 YES 출력