def solution(m, n, puddles):
    answer = 0

    # n x m 격자를 만든다
    grid = [
        [0 for _ in range(m + 1)]
        for _ in range(n + 1)
    ]

    # 시작점 세팅
    grid[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if (i, j) == (1, 1) or [j, i] in puddles:
                continue
            else:
                grid[i][j] = (grid[i-1][j] + grid[i][j-1]) % 1_000_000_007

    return grid[n][m]
