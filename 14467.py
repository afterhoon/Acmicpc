## 소가 길을 건너간 이유1
## https://www.acmicpc.net/problem/14467

n = int(input())
arr = [-1] * 11
ans = 0

# 등장하지 않은 소는 -1로 있고 최초 등장시 loc(0,1)을 입력한다
# 이후 등장했던 소는 arr%10과 loc을 확인해서 같으면 넘기고 같으면 
# 카운트를 arr의 10의 자리에 입력하고 1의 자리에 바뀐 loc을 입력한다
for i in range(n):
    cow, loc = map(int, input().split())
    if arr[cow] == -1:
        arr[cow] = loc
    elif arr[cow]%10 != loc:
        arr[cow] = (arr[cow]//10 + 1)*10 + loc

for i in range(1,11):
    if arr[i] > -1:
        ans += arr[i]//10

print(ans)