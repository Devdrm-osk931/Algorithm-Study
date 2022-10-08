N, K = tuple(map(int, input().split()))
items = [[0, 0]]
for _ in range(N):
    items.append(list(map(int, input().split())))

# # dp[i][j] => i 번째 item까지 봤을 때 j 가방 안에 담을 수 있는 최대 가치
# dp = [
#     [0 for _ in range(K + 1)]
#     for _ in range(N + 1)
# ]
#
#
# for i in range(1, N + 1):
#     for j in range(1, K + 1):
#         weight = items[i][0]
#         value = items[i][1]
#
#         if weight > j:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
#
# for row in dp:
#     for elem in row:
#         print(elem, end= ' ')
#     print()

dp = [0 for _ in range(K + 1)]
for i in range(1, N + 1):
    for j in range(K, 0, -1):
        if items[i][0] <= j:
            dp[j] = max(dp[j], dp[j - items[i][0]] + items[i][1])
print(dp)