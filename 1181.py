## 단어 정렬
## https://www.acmicpc.net/problem/1181

n = int(input())
word = [[] for i in range(51)]
# word[글자수만큼의 인덱스] 에 각 단어를 입력
for _ in range(n):
    temp = input()
    word[len(temp)].append(temp)

# 각각 중복 제거후 정렬해준다
for i in range(51):
    word[i] = sorted(list(set(word[i])))

# 순서에 맞게 출력해준다
for i in range(51):
    size = len(word[i])
    if size != 0:
        print("\n".join(word[i]))