## 별 찍기 - 9
## https://www.acmicpc.net/problem/2446

n = int(input())
for i in range(n-1): #윗부분
    for j in range(i):
        print(end=" ")
    for j in range((n-i-1)*2+1):
        print(end="*")
    print()
for i in range(n): #아랫부분
    for j in range(n-i-1):
        print(end=" ")
    for j in range(i*2+1):
        print(end="*")
    print()