## 특별한 날
## https://www.acmicpc.net/problem/10768

m = int(input())
d = int(input())

# 달과 일을 합치고 218 앞은 before로 뒤는 after로 출력한다
day = m * 100 + d
event = "Special"
if day < 218:
    event = "Before"
elif day > 218:
    event = "After"

print(event)