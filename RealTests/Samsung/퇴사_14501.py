n = int(input())
time = []
profit = []
dp = [0] * (n + 1)

for _ in range(n):
    a, b = tuple(map(int, input().split()))
    time.append(a)
    profit.append(b)

for i in range(n - 1, -1, -1):
    if time[i] + i > n:
        dp[i] = dp[i + 1]
        continue

    dp[i] = max(dp[i + 1], profit[i] + dp[i + time[i]])

print(dp[0])
