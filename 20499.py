## Darius님 한타 안 함?
## https://www.acmicpc.net/problem/20499

k, d, a = map(int, input().split('/'))
print("hasu" if (k + a < d) or (d == 0) else "gosu")