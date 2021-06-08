## 거리의 합
## https://www.acmicpc.net/problem/2399

import sys
n = int(sys.stdin.readline())
x = list(map(int, input().split()))
tot = 0
sum = 0

x.sort()
## 점들을 정렬시키고 모든 점을 가장 끝부분의 점과 이어서 선분으로 만든다
for i in range(n-1):
    tot += x[n-1] - x[i]

## 가장 짧은 선분의 길이만큼 모든 선분의 길이를 빼준다
for i in range(n-1):
    sum += tot
    tot -= (x[n-1-i] - x[n-2-i]) * (n-1-i)

## 각 점을 이은 선분은 A-B와 B-A 두 경우가 존재하므로 sum값을 두배로 해준다
print(sum*2)

## EX) 5
##     1 5 3 2 4
##
## 1) 정렬한다
##     1 2 3 4 5
##
## 2) 선분으로 만든다
##     1 2 3 4 5
##      ㅡㅡㅡㅡ
##        ㅡㅡㅡ
##          ㅡㅡ
##            ㅡ    >> sum: 0 tot: 10
##
## 3) 가장 짧은 선분 길이만큼 제외한다
##      ㅡㅡㅡ
##        ㅡㅡ
##          ㅡ      >> sum: 10 tot: 6
##
## 4) 반복한다
##      ㅡㅡ
##        ㅡ        >> sum: 16 tot: 3
##
##      ㅡ          >> sum: 19 tot: 1
##                  >> sum: 20 tot: 0
##
## 5) 각 점을 이은 선분은 A-B와 B-A 두 경우가 존재하므로 sum값을 두배로 해준다 result = sum * 2 = 40
