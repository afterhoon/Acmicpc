## 와글와글 숭고한
## https://www.acmicpc.net/problem/17388

s, k, h = map(int, input().split())
if s + k + h >= 100:
    print("OK")
else:
    low = min(s, k, h)
    if low == s:
        print("Soongsil")
    elif low == k:
        print("Korea")
    else:
        print("Hanyang")