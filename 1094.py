## 막대기
## https://www.acmicpc.net/problem/1094

x = int(input())
stick = 64
ans = 0
while True:
    if x < stick: #막대기가 원하는 길이보다 크다면 반으로 자른다
        stick /= 2
    elif x == stick: #막대기가 남은 길이와 같다면 카운트를 +1하고 종료한다
        ans += 1
        break
    else: #막대기가 남은 길이보다 작다면 더해주고 카운트를 +1 한다
        ans += 1
        x -= stick

print(ans)