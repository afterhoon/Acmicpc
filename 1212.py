## 8진수 2진수
## https://www.acmicpc.net/problem/1212

n = int(input(), 8) #8진수로 입력받음
print("{}".format(bin(n))[2:]) #앞의 0b는 빼고 출력한다