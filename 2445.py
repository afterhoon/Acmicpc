## 별 찍기 -8
## https://www.acmicpc.net/problem/2445

# 재귀적으로 print_star 출력. 가운데로 갈수록 별이 많아짐
# k == n 이 되면 중앙이므로 함수를 종료
def star(n, k):
    if k == n:
        print_star(n, k)
        return
    print_star(n, k)
    star(n, k+1)
    print_star(n, k)

# n*2개의 문자중 k*2개의 별을 출력한다
def print_star(n, k):
    for i in range(n):
        if i < k:
            print("*", end='')
        else:
            print(" ", end='')
    for i in range(n):
        if n-i-1 < k:
            print("*", end='')
        else:
            print(" ", end='')
    print()

n = int(input())
star(n, 1)