## 이름궁합 테스트
## https://www.acmicpc.net/problem/17269

alp = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
n, m = map(int, input().split())
a, b = input().split()
s = []
cnt = 0
while cnt < max(n, m): #a와 b의 이름을 합친 문자열 생성
    if cnt < n:
        s.append(alp[ord(a[cnt])-65])
    if cnt < m:
        s.append(alp[ord(b[cnt])-65])
    cnt += 1

for i in range(n+m-2):
    for j in range(n+m-1-i):
        s[j] = (s[j] + s[j+1]) % 10 #현재원소와 다음원소를 합한 수의 1의 자리 숫자로 교체
    s.pop() #맨 마지막 원소는 더미이므로 버린다
    
print(s[0]*10+s[1], end="%\n") #숫자로 치환해서 출력