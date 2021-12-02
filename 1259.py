## 팰린드롬수
## https://www.acmicpc.net/problem/1259

while True:
    ans = "yes"
    n = list(input())
    if n[0] == '0':
        break

    for i in range(len(n)//2):
        # 펠린드롬수는 좌우 대칭인 수 이므로
        # 맨 앞과 맨 뒤부터 비교한다
        if n[i] != n[-i-1]:
            ans = "no"
            break
    print(ans)