## 세로읽기
## https://www.acmicpc.net/problem/10798

arr = []
largest = 0
res = ""
for i in range(5):
    arr.append(list(input()))
    largest = max(largest, len(arr[i])) # 가장 긴 문자열 찾기

for i in range(largest): # 가장 긴 문자열의 길이만큼 반복한다
    for j in range(len(arr)): # 매 반복마다 첫번째~마지막 문자열을 순회
        if len(arr[j]) > i: # 문자열의 길이가 i보다 작으면 계산할 수 없으므로 건너 뛴다
            res += arr[j][i]

print(res)