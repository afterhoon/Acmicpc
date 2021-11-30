## 스타후르츠
## https://www.acmicpc.net/problem/17496

n, t, c, p = map(int, input().split())
print((n-1)//t*c*p) 
#첫날은 제외하므로 n-1이고 날짜가 지나면 수확할 수 없으므로 
#나머지를 제외한 몫으로 값을 구한다