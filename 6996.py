## 애너그램
## https://www.acmicpc.net/problem/6996

'''
3
blather reblath
maryland landam
bizarre brazier
'''

t = int(input())
for _ in range(t):
    a, b = map(list, input().split()) #문자열 a,b를 리스트로 받는다
    print("".join(a), "&", "".join(b), "are ", end="")
    if sorted(a) != sorted(b): #두 문자열을 정렬한 뒤 비교한다
        print("NOT ", end="")
    print("anagrams.")
