## N과 M (6)
## https://www.acmicpc.net/problem/15655

# temp 리스트에 정해진 길이까지 저장한후 완성되면 출력
# 출력한 뒤에는 맨 뒤의 원소를 pop으로 제거해준다
def func(start, index):
    if index == 0:
        print(" ".join(map(str, temp)))
        return

    for i in range(start, n):
        temp.append(arr[i])
        func(i+1, index-1)
        temp.pop()

n, m = map(int, input().split())
temp = []
arr = list(map(int, input().split()))
arr.sort()

func(0, m)