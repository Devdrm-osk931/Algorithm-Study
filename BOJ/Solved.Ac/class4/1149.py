# BOJ_class4_1149_silver1
"""
아래 규칙을 만족하면서 모든 집을 칠하는 비용의 최솟값을 구해보자

- 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
- N번 집의 색은 N-1번 집의 색과 같지 않아야 한다.
- i(2 ≤ i ≤ N-1)번 집의 색은 i-1번, i+1번 집의 색과 같지 않아야 한다.
"""

"""
완전탐색을 통해 가능한 조합들을 다 찾은 뒤 최소 값을 구하는 방법 - 시간초과
import sys

N = int(input())
costs = []
for _ in range(N):
    costs.append(list(map(int, input().split())))

# 0, 1, 2 중 하나를 선택하는 식으로 N개를 선택한다 -> 인접한 색은 달라야한다
case = []
minimum_cost = sys.maxsize
def dfs(depth):
    global minimum_cost
    if depth == N:
        case_cost = 0
        for i, color in enumerate(case):
            case_cost += costs[i][color]
        minimum_cost = min(minimum_cost, case_cost)
        return
    for color in range(3):
        if not case or case[-1] != color:
            case.append(color)
            dfs(depth + 1)
            case.pop()

dfs(0)
print(minimum_cost)
"""

"""
DP
"""
import sys
si = sys.stdin.readline

n = int(si())
# 최소 케이스를 담고있는 2-D List
RGB = [
    list(map(int, si().strip().split()))
    for _ in range(n)
]

for i in range(1, n):
    RGB[i][0] = min(RGB[i-1][1], RGB[i-1][2]) + RGB[i][0]
    RGB[i][1] = min(RGB[i-1][0], RGB[i-1][2]) + RGB[i][1]
    RGB[i][2] = min(RGB[i-1][0], RGB[i-1][1]) + RGB[i][2]

print(min(RGB[n-1]))