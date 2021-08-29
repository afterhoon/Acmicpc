## 좋다
## https://www.acmicpc.net/problem/1253

n = int(input())
num = list(map(int, input().split()))
num.sort()
cnt = 0

for i in range(n):
    # 정렬된 각 원소마다 해당 원소가 빠져있는 리스트를 생성한 후
    # 좌우 끝의 원소의 인덱스를 구해준다
    arr = num[:i] + num[i+1:]
    left, right = 0, n-2

    # 리스트 좌우 끝의 원소를 더해 해당 원소와 같은 값인지 확인한다
    # 해당 원소보다 크면 right를 1 감소, 작으면 left를 1 증가시키며
    # 찾지 못하면 cnt를 올리지 않고 다음 원소로 넘어간다
    while left < right:
        sum = arr[left] + arr[right]
        if num[i] == sum:
            cnt += 1
            break
        elif num[i] > sum:
            left += 1
        else:
            right -= 1

print(cnt)