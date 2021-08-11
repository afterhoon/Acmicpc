## 배수와 약수
## https://www.acmicpc.net/problem/5086

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    case = "factor"
    cnt = 0

    if a > b:
        temp = a
        a = b
        b = temp
        case = "multiple"

    while True:
        cnt += 1

        if a*cnt == b:
            break
        if a*cnt > b:
            case = "neither"
            break

    print(case)