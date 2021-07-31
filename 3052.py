## 나머지
## https://www.acmicpc.net/problem/3052

arr = []
for i in range(10):
    temp = int(input()) % 42
    arr.append(temp)
# set으로 변환해서 중복을 모두 제거해준다 (서로 남은 나머지만 남음)
print(len(list(set(arr))))