## A+B -4
## https://www.acmicpc.net/problem/10951

# try문이 없을경우 EOF Error가 발생했다 예외처리를 하니 통과
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except:
        break