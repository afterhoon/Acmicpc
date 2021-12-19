## 뉴비의 기준은 뭘까?
## https://www.acmicpc.net/problem/19944

n, m = map(int, input().split())
if m < 3:
    print("NEWBIE!")
else:
    if n < m:
        print("TLE!");
    else:
        print("OLDBIE!");