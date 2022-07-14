# BOJ_11501_주식_실버2

t = int(input())
for _ in range(t):
    n = int(input())
    prices = list(map(int, input().split()))
    largest = -1
    ans = 0

    for idx in range(n-1, -1, -1):
        if prices[idx] > largest:
            largest = prices[idx]

        else:
            ans += largest - prices[idx]

    print(ans)
