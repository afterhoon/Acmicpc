## 줄 세우기
## https://www.acmicpc.net/problem/2252

N, M = map(int, input().split())
arr = [[] for i in range(N+1)]
depth = [0] * (N+1)
queue = []
ans = []

## 각 케이스에서 뒤에 학생은 반드시 앞의 학생보다는 크므로 depth를 하나씩 추가해준다 (depth가 작을수록 앞, 클수록 뒤)
for i in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    depth[b] += 1

## depth가 0이면 반드시 맨 앞 이기 때문에 queue에 추가해준다
for i in range(1, N+1):
    if depth[i] == 0:
        queue.append(i)

## queue에 있는 원소를 먼저 ans리스트에 넣어주고
## 그 원소의 뒤에 있던 학생의 depth를 1 낮춰주고 만약 depth가 0이된다면 queue에 입력해준다
## 이 과정을 반복해주면 depth가 작은 순으로 출력해서 키순서로 정렬이 된다
while queue:
    for i in queue:
        temp = i
        queue.remove(i)
        ans.append(temp)
        for j in arr[temp]:
            depth[j] -= 1
            if depth[j] == 0:
                queue.append(j)
        
for i in ans:
    print(i, end=" ")