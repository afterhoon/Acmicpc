## 단어 뒤집기
## https://www.acmicpc.net/problem/9093

T = int(input())
for t in range(T):
    line = list(map(str, input().split()))
    
    # 문자열에서 각 단어마다 순서를 뒤집어서 출력한다
    for i in range(len(line)):
        print("".join(reversed(line[i])), end=" ")
    print()