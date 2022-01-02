## 괄호
## https://www.acmicpc.net/problem/9012

t = int(input())
for _ in range(t):
    ps = list(input())
    cnt = 0
    vps = True

    for i in ps:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1

        if cnt < 0: # 모든 경우에서 ')'는 항상 '(' 보다 적은 개수여야 한다
            vps = False
            break
    if cnt != 0: # 모든 검사가 끝나고 '('와 ')'의 수가 다르면 vps가 아니다
        vps = False
    
    print("YES" if vps else "NO")

