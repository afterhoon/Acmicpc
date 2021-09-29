## 1, 2, 3 더하기 2
## https://www.acmicpc.net/problem/12101

def func(n, s):
    # n이 0이라면 정상적으로 모든 수가 1,2,3 의 수로 변환된 것이므로 arr에 저장
    if n == 0:
        arr.append(s)
    
    # 1~3의 수를 문자열 s에 입력하고 재귀함수를 호출한다
    for i in range(1,4):
        if n-i >= 0:
            s += str(i)
            func(n-i, s)
            s = s[:-1]

n, k = map(int, input().split())
arr = []
func(n, "")

# k가 arr의 길이보다 크면 출력할것이 없으므로 -1 출력
try:
    print("+".join(arr[k-1]))
except:
    print("-1")

'''
n = 4 일 경우
문자열 s가 arr에 입력되는 과정
1 1 1 1
    2
  2 1
  3
2 1 1
  2
3 1
'''