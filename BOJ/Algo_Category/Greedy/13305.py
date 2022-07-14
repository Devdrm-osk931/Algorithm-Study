# BOJ_13305_주유소_실버4

n = int(input())
dists = list(map(int, input().split()))
costs = list(map(int, input().split()))
costs.pop()
answer = dists[0] * costs[0]

for i in range(1, len(costs)):
    if costs[i] >= costs[i-1]:
        costs[i] = costs[i-1]
    answer += dists[i] * costs[i]


print(answer)