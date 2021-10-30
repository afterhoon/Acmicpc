## 완전 제곱수
## https://www.acmicpc.net/problem/1977

m = int(input())
n = int(input())
arr = []
i = 1

# 제곱수가 n을 넘을때까지 반복
while i*i <= n:
    if m <= i*i <= n:
        arr.append(i*i) # 모두 arr에 저장한다
    i += 1

if not arr: # arr에 원소가 없다면 -1 출력
    print(-1)
else:
    print(sum(arr))
    print(arr[0])