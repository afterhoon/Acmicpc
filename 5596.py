## 시험 점수
## https://www.acmicpc.net/problem/5596

s = sum(list(map(int, input().split())))
t = sum(list(map(int, input().split())))
# s>t 일 경우 s, 아닐경우 t 와 같다
print(s if s > t else t)
