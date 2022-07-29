import sys
si = sys.stdin.readline

n = int(si())
nums = list(map(int, si().split()))

dp = [0] * n
dp[0] = nums[0]

for i in range(1, n):
    dp[i] = max(nums[i], dp[i-1] + nums[i])

print(max(dp))