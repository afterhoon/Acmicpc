## 토너먼트
## https://www.acmicpc.net/problem/1057

n, a, b = map(int, input().split())
cnt = 0

# 각 라운드마다 번호를 매긴다고 할때
# 1,2번중 승자를 2라운드의 1번, 3,4번중 승자가 2번이 된다
# 따라서 각 승자는 다음번에 x - x//2 의 번호를 배정 받는다
# 따라서 a와 b가 같은 숫자가 될때의 라운드에서 겨룬다고 할 수 있다
while a != b:
    a -= a // 2
    b -= b // 2
    cnt += 1
print(cnt)