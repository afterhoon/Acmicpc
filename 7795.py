## 먹을 것인가 먹힐 것인가
## https://www.acmicpc.net/problem/7795

# 반복문으로 단순 반복 계산을 하면 시간초과가 발생한다
# 이진검색으로 시간 단축
def binary_search(target, arr):
    start = 0
    end = len(arr) - 1
    res = -1
    while start <= end :
        mid = (start + end) // 2
        if arr[mid] < target:
            res = mid
            start = mid + 1
        else:
            end = mid - 1
    return res

T = int(input())
for t in range(T):
    n, m = map(int, input().split())
    # 검색을 위해 미리 a와 b를 정렬해준다
    a = sorted(list(map(int, input().split())))
    b = sorted(list(map(int, input().split())))
    cnt = 0

    for el in a:
        cnt += binary_search(el, b) + 1

    print(cnt)