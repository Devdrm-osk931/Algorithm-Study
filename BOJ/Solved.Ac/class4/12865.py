# BOJ_Class4_12856_평범한 배낭(Gold 5)

MAXIMUM = 100_000

N, K = tuple(map(int, input().split()))

items = []
dp = [0] * (K + 1)
# dp3 = [0] * (K + 1)

for _ in range(N):
    w, v = tuple(map(int, input().split()))
    items.append((w, v))

for w, v in items:
    for i in range(K, w - 1, -1):
        dp[i] = max(dp[i], dp[i - w] + v)

    # 왜 앞에서부터 하면 안되는지를 볼 수 있음
    # 앞에서부터 넣게 되면 지금 보고 있는 아이템을 넣은 결과를 참조하여 또 넣을 수 있는 문제점이 있음 --> 특정 아이템을 여러번 넣게 될 수 있는 가능성이 있음
    # 따라서 뒤에서부터 갱신을 해주어야 갱신된 값을 참조하는 문제를 방지할수 있음.
    """
    for i in range(w, K + 1):
        dp3[i] = max(dp3[i], dp3[i-w] + v)
        print("DP3", dp3)
    print()
    """

print(dp[-1])

dp2 = [
    [0 for _ in range(K + 1)]
    for _ in range(N + 1)
]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        if i == 0 or j == 0:
            dp2[i][j] = 0

        else:
            if j - items[i-1][0] >= 0:
                dp2[i][j] = max(dp2[i-1][j], dp2[i-1][j-items[i-1][0]] + items[i-1][1])
            else:
                dp2[i][j] = dp2[i-1][j]

# for row in dp2:
#     for elem in row:
#         print(elem, end=' ')
#     print()
#
# print(dp2[-1][-1])