# Programmers
# 멀리뛰기 Lv2

def solution(n):
    dp = [1, 2]

    if n == 1 or n == 2:
        return dp[n - 1]

    for i in range(2, n):
        dp.append((dp[i - 2] + dp[i - 1]) % 1234567)

    return dp[-1]

# 1
# 1 1, 2 0

# 1 1 1, 1 2, 2, 1
# dp[i] = dp[i - 1] + dp[i - 2]