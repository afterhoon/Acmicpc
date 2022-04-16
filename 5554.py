## 심부름 가는 길
## https://www.acmicpc.net/problem/5554

sec = 0
for i in range(4):
	sec += int(input())
print(sec // 60)
print(sec % 60)