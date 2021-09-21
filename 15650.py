## N과 M (2)
## https://www.acmicpc.net/problem/15650

def dfs(k):
    if len(arr)==m:
        print(' '.join(map(str,arr)))
        return
    
    # 작은자리수부터 나와야 하므로 k로 앞 인덱스를 잡아준다
    for i in range(k,n+1):
        if i not in arr:
            arr.append(i)
            dfs(i+1)
            arr.pop()

n,m = list(map(int,input().split()))
arr = []

dfs(1)