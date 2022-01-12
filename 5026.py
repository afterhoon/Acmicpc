## 박사 과정
## https://www.acmicpc.net/problem/5026

n = int(input())
for _ in range(n):
    temp = input()
    if (temp == "P=NP"):
        print("skipped")
    else:
        a, b = map(int, temp.split("+"))
        print(a+b)
