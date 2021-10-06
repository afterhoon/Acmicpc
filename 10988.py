## 펠린드롬인지 확인하기
## https://www.acmicpc.net/problem/10988

word = input()
ans = 1

for i in range(len(word)//2):
    # 맨 앞과 맨 뒤부터 비교해가며 다른 문자가 나오면 
    # ans를 0으로 바꾼뒤 반복종료
    if word[i] != word[len(word)-1-i]:
        ans = 0
        break

print(ans)