# BOJ 11056
# 가장 긴 바이토닉 부분 수열

n = int(input())
numbers = list(map(int, input().split()))

# i 번째 요소를 마지막으로 하는 수열의 최대 길이
dp = [1 for _ in range(n)]

# 먼저 최대한 증가하는 수열을 생각한다
for curr_idx in range(1, n):
    for prev_idx in range(curr_idx):
        if numbers[curr_idx] > numbers[prev_idx]:
            dp[curr_idx] = max(dp[curr_idx], dp[prev_idx] + 1)


# 감소하는 부분을 생각한다
for curr_idx in range(1, n):
    for prev_idx in range(curr_idx):
        if numbers[curr_idx] < numbers[prev_idx]:
            dp[curr_idx] = max(dp[curr_idx], dp[prev_idx] + 1)

print(max(dp))
