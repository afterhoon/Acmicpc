## 짝수를 찾아라
## https://www.acmicpc.net/problem/3058

T = int(input())
for t in range(T):
    n = list(map(int, input().split()))
    sum = 0
    minimum = 101
    for i in range(len(n)):
        # 짝수일 경우 sum에 더해주고 최소값과 비교해 더 낮으면 바꿔준다
        if n[i]%2 == 0:
            sum += n[i]
            if n[i] < minimum:
                minimum = n[i]
    print(sum, minimum)