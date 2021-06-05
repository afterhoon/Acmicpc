## 초콜릿 자르기
## https://www.acmicpc.net/problem/2163

## 가로가 N 세로가 M이라고 할때 가로부터 자르면 N-1회 자른다
## 세로로 자를때는 N개의 1xM 크기의 초콜릿을 잘라야하므로 (M-1)*N 회 자른다
## 따라서 (N-1)+(M-1)*N = N-1+MN-N = MN - 1
N, M = map(int, input().split())
print(N*M-1)