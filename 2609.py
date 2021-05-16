## 2609 최대공약수와 최소공배수
## https://www.acmicpc.net/problem/2609

# 숫자 2개를 입력받고 임시 변수에 복사
n1, n2 = map(int, input().split())
a, b = n1, n2

# 유클리드 호제법으로 a에 최대공약수 입력
while b != 0:
    temp = a % b
    a = b
    b = temp

# a = 최대공약수
print(a)

# n1*n2에서 최대공약수를 나누어주면 최소공배수 출력
print(n1*n2//a)