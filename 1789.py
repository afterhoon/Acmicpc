## 수들의 합
## https://www.acmicpc.net/problem/1789

import sys
# 입력사양이 4,294,967,295 까지기 때문에 int로 수행하면 오버플로우가 발생하므로
# unsigned int를 사용해야하지만 파이썬이므로 생략한다
s = int(sys.stdin.readline())
res = 0
cnt = 0

# 숫자 s를 서로 다른 n개의 자연수로 만드는 방법은 1+2+3+... > s 가 되는 때의 숫자의 개수와 같다
# cnt 변수로 등차수열로 더해주면되는데 자연수 1부터 시작이므로 cnt+1을 해주었다
while res <= s:
    res += cnt + 1
    cnt += 1

# 구해진 cnt은 숫자 s를 초과한 값이기 때문에 맞춰주기 위해 같은 자연수를 써야하므로 1을 빼준다
print(cnt-1)