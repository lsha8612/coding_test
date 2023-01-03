import sys
input = sys.stdin.readline

# n=수열의 개수, m=나누어떨어져야 하는 수
n, m = map(int, input().split())
# 원본 리스트
A = list(map(int, input().split()))
# 구간합 리스트
S = [0] * n
# 나머지 값을 저장하는 리스트
C = [0] * m

S[0] = A[0]
# 합 배열 만들기
for i in range(1, n):
    S[i] = S[i-1] + A[i]

# 정답 변수
answer = 0
# 합 배열의 모든 값에 %연산 실행
for i in range(n):
    remain = S[i] % m
    if remain == 0:
        answer += 1
    C[remain] += 1

# 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
for i in range(m):
    if C[i] > 1:
        answer += (C[i] * (C[i]-1) // 2)

print(answer)
