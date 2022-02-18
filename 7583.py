## Jumbled Words
## https://www.acmicpc.net/problem/7583

while True:
    s = list(input().split())
    if s[0] == "#":
        break
    for i in range(len(s)):
        # 문자열을 뒤집는다
        temp = ""
        for c in s[i]:
            temp = c + temp

        # 문자열의 맨앞과 맨뒤를 바꾼다
        temp = list(temp)
        temp[0], temp[-1] = temp[-1], temp[0]
        s[i] = "".join(temp)
    print(" ".join(s))