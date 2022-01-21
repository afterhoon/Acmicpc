## 시각
## https://www.acmicpc.net/problem/18312

n, k = map(int, input().split())
k = str(k)
cnt = 0
for i in range(n+1):
    i = str(i) if i > 9 else "0" + str(i) # 시간이 10 미만이면 0 추가
    for j in range(60):
        j = str(j) if j > 9 else "0" + str(j) # 분이 10 미만이면 0 추가
        for l in range(60):
            l = str(l) if l > 9 else "0" + str(l) # 초가 10 미만이면 0 추가
            if k in (i+j+l): # hh:mm:ss 에 k가 포함되면 카운트 +1
                cnt += 1
print(cnt)