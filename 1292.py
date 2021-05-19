## 쉽게 푸는 문제
## https://www.acmicpc.net/problem/1292

a, b = map(int,input().split());
count = 0;
sum = 0;

arr = [];
for i in range(1000):
    for j in range(i):
        count = count + 1;
        arr.append(i);
    if(count == b):
        break;

for i in range(a-1,b):
    sum = sum + arr[i];

print(sum);