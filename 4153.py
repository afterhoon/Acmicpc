## 직각삼각형
## https://www.acmicpc.net/problem/4153

while True:
    a, b, c = map(int, input().split());
    if a==b==c==0:
        break
    
    ## 각 변의 값을 오름차순으로 정렬
    x = min(a,b,c)
    z = max(a,b,c)
    y = (a+b+c) - (x+z)

    if x*x + y*y == z*z:
        print("right")
    else:
        print("wrong")