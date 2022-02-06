## 점수 계산
## https://www.acmicpc.net/problem/2822

arr = []
idx = []
for _ in range(8):
    arr.append(int(input()))

# 점수 상위 5개를 temp에 입력
temp = sorted(arr, reverse=True)
temp = temp[:5]
for i in temp:
    # 상위 점수 5개에 대한 인덱스를 idx에 입력
    idx.append(arr.index(i)+1)

print(sum(temp)) # 상위 점수 5개의 합
print(" ".join(map(str, sorted(idx)))) # idx를 정렬한 뒤 출력