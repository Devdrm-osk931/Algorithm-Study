# Samsung study

MIN = -1e9


N = int(input())

s = [0 for _ in range(N + 1)]
e = [0 for _ in range(N + 1)]
p = [0 for _ in range(N + 1)]

for i in range(1, N + 1):
    e[i], p[i] = tuple(map(int, input().split()))
    s[i], e[i] = i, i + e[i] - 1

dp = [MIN for _ in range(N + 1)]
dp[0] = 0

for i in range(1, N + 1):
    if e[i] > N:
        continue

    for j in range(0, i):
        if e[j] < s[i]:
            dp[i] = max(dp[i], dp[j] + p[i])


print(max(dp))
