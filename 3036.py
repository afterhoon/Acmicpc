## 링
## https://www.acmicpc.net/problem/3036

def gcd(x,y):
    while y:
        x, y = y, x%y
    return x

n = int(input())
arr = list(map(int, input().split()))
for i in range(1, n):
    # 분자(arr[0])과 분모(arr[i])를 최대공약수로 나눠주고 출력한다
    temp = gcd(arr[0], arr[i])
    print("%d/%d" % (arr[0] // temp, arr[i] // temp))