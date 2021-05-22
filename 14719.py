## 빗물
## https://www.acmicpc.net/problem/14719

H, W = map(int, input().split())
arr = list(map(int, input().split()))
temp = []

left = 0
right = 0
count = 0
sum = 0

for i in arr:
    count = count + 1
    if i > left or count == W:
        right = i

        height = min(left, right)
        for j in temp:
            sum = sum + (height-j)

        left = i
        right = 0
        temp = []
    elif i < left:
        temp.append(i)

print(sum)
