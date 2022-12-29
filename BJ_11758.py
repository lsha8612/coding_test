import sys
input = sys.stdin.readline

#3개의 점 입력받기
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

#CCW 공식
CCW = (x1 * y2 + x2 * y3 + x3 * y1) - (x2 * y1 + x3 * y2 + x1 * y3)

if CCW > 0:
    print(1)
elif CCW < 0:
    print(-1)
else:
    print(0)