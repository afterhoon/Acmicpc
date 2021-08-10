## 소트인사이드
## https://www.acmicpc.net/problem/1427

n = input()
arr = []
# 입력받은 문자열을 리스트로 변환한다
for i in range(len(n)):
    arr.append(n[i])
# 내림차순으로 정렬한뒤 공백없이 출력한다
print(''.join(sorted(arr, reverse=True)))