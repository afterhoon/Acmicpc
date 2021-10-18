## 단어 뒤집기 2
## https://www.acmicpc.net/problem/17413

s = input()
buffer = "" # 특정 문자가 나올때까지 문자열을 받아들인다
mode = 0    # 0: INSERT , 1: READ
for i in range(len(s)):
    if mode == 0:
        if s[i] == " ":
            print(buffer[::-1], end=" ")
            buffer = ""
            continue
        elif s[i] == "<":
            print(buffer[::-1], end="")
            print("<", end="")
            buffer = ""
            mode = 1 # 괄호 안의 문자열은 그대로 출력해야하므로 
                     # mode = 1(READ) 로 변경
            continue
        buffer += s[i]
    elif mode == 1: # 괄호 안이므로 그대로 출력한다
        print(s[i], end="")
        if s[i] == ">": # 괄호가 끝나면 mode를 0(INSERT)로 바꾼다
            mode = 0
print(buffer[::-1]) # 버퍼에 남은 문자열을 처리한다