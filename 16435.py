## 스네이크버드
## https://www.acmicpc.net/problem/16435

n, l = map(int, input().split())
h = sorted(list(map(int, input().split())))

# 과일들을 크기순으로 정렬한 뒤 l보다 작거나 같은 과일을 발견하면
# l의 크기를 1 늘려준다
for el in h:
    if l >= el:
        l += 1
print(l)
