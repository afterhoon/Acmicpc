## 진법
## https://www.acmicpc.net/problem/2745

# 아스키값을 이용해 문자들을 그에 맞는 숫자로 변환해주는 함수
def function(n):
    num = ord(n)
    if num>=ord('0') and num<=ord('9'):
        return num-ord('0')
    else:
        return num-ord('A')+10

a, b = map(str, input().split())
b = int(b)
length = len(a)
res = 0

# 각 자리수마다 진수의 거듭제곱을 해서 10진수에서의 값으로 변환
for i in range(length):
    res += function(a[i]) * pow(b, length-(i+1))

print(res)