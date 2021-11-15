## N과 M (7)
## https://www.acmicpc.net/problem/15656

n, m = map(int, input().split())
arr = sorted(list(map(int, input().split())))
temp = []

def func(depth):
    if depth == 0:
        print(' '.join(map(str, temp)))
        return
    
    for i in range(n):
        temp.append(arr[i])
        func(depth-1) # 수열을 한칸씩 입력한 뒤 재귀함수를 호출해준다
        temp.pop() # 다음 수열을 위해 제거해준다

func(m)