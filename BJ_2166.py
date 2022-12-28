#나머지 합 구하기_백준 2166번

import sys
input = sys.stdin.readline
n = int(input())
x = [0]
y = [0]

# n개의 x, y좌표를 입력 받음
for i in range(n):
    tempx, tempy = map(int, input().split())
    x.append(tempx)
    y.append(tempy)

# 마지막에 처음 점 다시 넣기
x.append(x[0])
y.append(y[0])

result = 0
for i in range(n):
    result += ((x[i]*y[i+1]) - (x[i+1]*y[i]))

print(round(abs(result/2), 1))
