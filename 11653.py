## 소인수분해
## https://www.acmicpc.net/problem/11653

n = int(input())
i = 2
while n >= i:
    # 2부터 나눠지는 숫자를 출력해준다
    if n % i == 0:
        n = n // i
        print(i)
    # 나눠지지 않는다면 1 증가시킨다
    else:
        i += 1
