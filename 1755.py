## 숫자놀이
## https://www.acmicpc.net/problem/1755

# 각 숫자의 우선순위를 담은 리스트 num 생성
num = ["9", "4", "8", "7", "2", "1", "6", "5", "0", "3"]
ans = []
msg = ""
m, n = map(int, input().split())

# m~n 까지 ans 리스트에 해당 숫자를 
# num으로 치환한 우선순위로 입력한다
for i in range(m, n+1):
    temp = str(i)
    k = ""
    for j in temp:
        k += num[int(j)]
    ans.append([i, k])

# 정렬한 후 한 줄에 10개씩 출력한다
ans.sort(key=lambda x:x[1])
for i in range(len(ans)):
    msg += str(ans[i][0])
    if i%10 == 9 or i == len(ans)-1:
        print(msg)
        msg = ""
    else:
        msg += " "