# BOJ_9251_LCS_Gold5

string_A = input()
string_B = input()

row = len(string_B)
col = len(string_A)

dp = [
    [0 for _ in range(col + 1)]
    for _ in range(row + 1)
]

for i in range(1, row + 1):
    for j in range(1, col + 1):
        if string_A[j - 1] != string_B[i - 1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        else:
            dp[i][j] = dp[i-1][j-1] + 1

print(dp[-1][-1])