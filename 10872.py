## 팩토리얼
## https://www.acmicpc.net/problem/10872

# 재귀함수로 팩토리얼을 구현한다
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

n = int(input())
print(factorial(n))