## 요세푸스 문제
## https://www.acmicpc.net/problem/1158

N, K = map(int, input().split())
count = 0
n = 0
arr = [i+1 for i in range(N)]

print(end="<")
while(arr):
    if count%K==K-1:
        print(arr[count], end="")
        n += 1
        if n == N:
            break
        print(end=", ")
    else:
        arr.append(arr[count])
    count += 1
print(">")