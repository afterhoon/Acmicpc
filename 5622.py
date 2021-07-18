## 다이얼
## https://www.acmicpc.net/problem/5622

str = input()
# 각 다이얼을 돌리는데 해당하는 시간을 미리 입력해놓는다
arr =[3+i//3 for i in range(15)] + [8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]
sec = 0
# 각 알파벳의 번호순으로 arr에 걸리는 시간을 입력해 놓았으므로
# arr을 이용해서 sec에 더해준다
for i in range(len(str)):
    sec += arr[ord(str[i]) - ord('A')]
print(sec)