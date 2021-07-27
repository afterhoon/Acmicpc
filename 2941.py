## 크로아티아 알파벳
## https://www.acmicpc.net/problem/2941

str = input()
length = len(str)
cnt = 1
# 문자열 길이가 1 이하이면 글자수는 길이와 같음
if length <= 1:
    cnt = length

# 크로아티아 알파벳중 특별한 값은 끝이 '=', '-', 'j' 중 하나이므로 이를 기준으로 판단
for i in range(1, length):
    if str[i] == '=' and str[i-1] == 'z' and str[i-2] == 'd':
        cnt -=1
    if str[i] == '=' and (str[i-1] in ['c', 's', 'z']):
        continue
    elif str[i] == '-' and (str[i-1] in ['c', 'd']):
        continue
    elif str[i] == 'j' and (str[i-1] in ['l', 'n']):
        continue
    else:
        cnt += 1

print(cnt)