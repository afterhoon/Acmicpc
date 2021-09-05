## 과자
## https://www.acmicpc.net/problem/10156

k, n, m = map(int, input().split())
print(max(k*n - m, 0))  ## 가진돈이 더 많으면 용돈이 필요없으므로 0 아래면 0출력