## 마인크래프트
## https://www.acmicpc.net/problem/18111

# 시간초과
import sys
N, M, B = map(int, sys.stdin.readline().split())
time = 205600000
height = 0
arr = []
arrVar = []
for i in range(N):
    temp = list(map(int, sys.stdin.readline().split()))
    for j in range(len(temp)):
        arrVar.append(temp[j])
    arr.append(temp)
arrVar = sorted(list(set(arrVar)))

for i in range(len(arrVar)):
    under = 0
    upper = 0
    for n in range(N):
        for m in range(M):
            if arr[n][m] < arrVar[i]:
                under += arrVar[i] - arr[n][m]
            else:
                upper += arr[n][m] - arrVar[i]
    block = upper + B
    if block < under:
        continue
    
    temp = upper * 2 + under
    if time > temp:
        time = temp
        height = arrVar[i]
print(time, height)