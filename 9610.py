## 사분면
## https://www.acmicpc.net/problem/9610

n = int(input())
arr = [0, 0, 0, 0, 0]
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        arr[0] += 1
    elif x > 0:
        if y > 0:
            arr[1] += 1
        else:
            arr[4] += 1
    else:
        if y > 0:
            arr[2] += 1
        else:
            arr[3] += 1

for i in range(1, 5):
    print("Q", i, ": ", arr[i], sep="")
print("AXIS:", arr[0])