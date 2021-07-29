## Java Bitecode
## https://www.acmicpc.net/problem/21867

bite = ['J', 'A', 'V']
n = input()
s = input()
# 문자열에서 bite리스트에 있는 문자를 제외하고 출력
s = ''.join(i for i in s if i not in bite)
# 문자열이 비어있다면 nojava 출력
print(s if s!="" else 'nojava')