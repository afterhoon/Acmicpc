## 나누기
## https://www.acmicpc.net/problem/1075

n = int(input())
f = int(input())
ans = 0

# 가장 적은수부터 우선으로 찾기 위해
# 우선 입력값 n의 맨 뒷자리를 00으로 변경해준다
n = n - n%100
while True:
    # n + ans 가 f로 떨어지면 뒷자리를 출력한다
    if (n+ans) % f == 0:
        print("%02d" % (ans))
        break

    # 아니라면 1씩 증가시키며 수행한다
    ans += 1
