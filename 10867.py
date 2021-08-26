## 중복 빼고 정렬하기
## https://www.acmicpc.net/problem/10867

n = int(input())

# set로 중복을 제거하고 sorted()함수로 정렬한다
arr = map(str, sorted(set(map(int, input().split()))))
print(" ".join(arr))