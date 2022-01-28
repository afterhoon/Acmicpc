## 5와 6의 차이
## https://www.acmicpc.net/problem/2864

a, b = map(str, input().split())

# 최솟값을 구할 때는 모든 6을 5로 대체, 최댓값을 구할 때는 모든 5를 6으로 대체한다
print(int(a.replace('6', '5')) + int(b.replace('6', '5')), int(a.replace('5', '6')) + int(b.replace('5', '6')))
