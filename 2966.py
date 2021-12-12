## 찍기
## https://www.acmicpc.net/problem/2966

'''
ABC
BABC
CCAABB
'''

def isCorrect(arr, len, cnt, n): # 정답을 맞췄는지 체크
    return arr[cnt % len] == answer[cnt % n]

adrian = ['A', 'B', 'C']
bruno = ['B', 'A', 'B', 'C']
goran = ['C', 'C', 'A', 'A', 'B', 'B']
len = [3, 4, 6] #각각의 리스트의 길이
score = [0, 0, 0] #각각의 정답개수 리스트

n = int(input())
answer = list(input())

for i in range(n): # 매 문제마다 정답을 맞췄는지 확인
    score[0] += (1 if isCorrect(adrian, len[0], i, n) else 0)
    score[1] += (1 if isCorrect(bruno, len[1], i, n) else 0)
    score[2] += (1 if isCorrect(goran, len[2], i, n) else 0)

result = max(score)
print(result) # 가장 큰 점수 출력

# 최고점이 누구인지 출력 (중복가능)
print("Adrian") if result == score[0] else ""
print("Bruno") if result == score[1] else ""
print("Goran") if result == score[2] else ""