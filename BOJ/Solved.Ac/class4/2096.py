# BOJ 2096
# 내려가기
# import sys
# input = sys.stdin.readline

n = int(input())
max_dp = [0, 0, 0]
min_dp = [0, 0, 0]
max_temp = [0, 0, 0]
min_temp = [0, 0, 0]

for i in range(n):
    given = list(map(int, input().split()))
    if i == 0:
        max_dp = given[:]
        min_dp = given[:]

    else:
        # max/min 계산
        for idx in range(3):
            max_temp[idx] = 0
            min_temp[idx] = 0

        for idx in range(3):
            max_temp[0] = max(max_dp[0], max_dp[1]) + given[0]
            min_temp[0] = min(min_dp[0], min_dp[1]) + given[0]

            max_temp[1] = max(max_dp[0], max_dp[1], max_dp[2]) + given[1]
            min_temp[1] = min(min_dp[0], min_dp[1], min_dp[2]) + given[1]

            max_temp[2] = max(max_dp[1], max_dp[2]) + given[2]
            min_temp[2] = min(min_dp[1], min_dp[2]) + given[2]

        # max_dp/min_dp 에 temp 반영
        max_dp = max_temp[:]
        min_dp = min_temp[:]

print(max(max_dp), min(min_dp))
