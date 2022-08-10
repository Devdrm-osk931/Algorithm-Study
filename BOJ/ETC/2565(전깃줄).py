#BOJ_2565전깃줄_Gold5

n = int(input())
lines = [
    list(map(int, input().split()))
    for _ in range(n)
]

lines.sort(key=lambda x:x[0])

# lines의 한 요소 line -> line[1]을 기준으로 LIS의 길이를 구한다

dp = [1] * n

for i in range(n):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

# LIS를 위해 제거해야하는 줄의 최소 값은 n - max(dp)
print(n - max(dp))