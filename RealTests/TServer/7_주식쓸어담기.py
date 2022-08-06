def solution(money, stocks):
    answer = 0

    dp = [0] * (money + 1)

    for value, price in stocks:
        for i in range(money, price - 1, -1):
            dp[i] = max(dp[i], dp[i - price] + value)

    return dp[-1]