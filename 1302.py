## 베스트셀러
## https://www.acmicpc.net/problem/1302

n = int(input())
book = []
name = []
cnt = []
for _ in range(n):
    book.append(input())

name = sorted(list(set(book))) # 각 책이름을 하나씩 가진 배열을 만들고 정렬한다

# 각 책이름마다 개수를 확인한다
for x in name:
    cnt.append(book.count(x))

# 가장 많은 책을 발견하면 출력하고 종료한다 (이미 정렬해놓았으므로 따로 처리할 필요 없음)
high = max(cnt)
for i in range(len(cnt)):
    if cnt[i] == high:
        print(name[i])
        break