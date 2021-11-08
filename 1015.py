## 수열 정렬
## https://www.acmicpc.net/problem/1015

n = int(input())
arr = list(map(int, input().split()))
ans = [-1 for i in range(n)] #정답을 담을 리스트 ans

cnt = 0
while cnt < n:
    for i in range(n): 
        arr[i] -= 1         #각 숫자를 모두 -1 해주고 
        if arr[i] == 0:     #0이 된 원소가 있다면 
            ans[i] = cnt    #차례대로 순서를 매겨서 ans리스트의 해당하는 인덱스에 넣어준다
            cnt += 1
            
print(" ".join(map(str, ans)))