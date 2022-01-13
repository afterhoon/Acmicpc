## 문어 숫자
## https://www.acmicpc.net/problem/1864

arr = {'-': 0, '\\': 1, '(': 2, '@': 3, '?': 4, '>': 5, '&': 6, '%': 7, '/': -1}
while True:
    temp = list(input())
    length = len(temp)
    if temp[0] == '#':
        break

    res = 0
    for i in range(length):
        res += arr[temp[i]] * 8**(length-i-1)
    print(res)








'''
-는 0에 대응한다.
\는 1에 대응한다.
(는 2에 대응한다.
@는 3에 대응한다.
?는 4에 대응한다.
>는 5에 대응한다.
&는 6에 대응한다.
%는 7에 대응한다.
/는 -1에 대응한다.
'''