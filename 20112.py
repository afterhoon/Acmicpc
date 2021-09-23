## 사토르 마방진
## https://www.acmicpc.net/problem/20112

n = int(input())
arr = []
ans = "YES"
for i in range(n):
    temp = input()
    arr.append([])
    for j in range(n):
        arr[i].append(temp[j])

# 배열의 i와 j 를 바꿔서 비교했을때 
# 모두 같다면 사토르 마방진이다
for i in range(n):
    for j in range(i,n):
        if arr[i][j] != arr[j][i]:
            ans = "NO"

print(ans)