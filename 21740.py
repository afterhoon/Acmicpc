## 도도의 수학놀이
## https://www.acmicpc.net/problem/21740
## indexError
n = int(input())
arr = [0, 1, 2, -1, -1, 5, 9, -1, 8, 6]
a = list(map(int, input().split()))
b = []
ans = []
for i in range(n):
    b.append((arr[a[i]]))
b.sort()
if n != 1:
    if b[0] == 0:
        for i in range(n):
            if b[i] != 0:
                b[0], b[i] = b[i], b[0]
                break
                
for i in range(n):
    ans.append(arr[b[i]])
ans.append(ans[n-1])
print("".join(map(str, ans)) if sum(ans) else 0)