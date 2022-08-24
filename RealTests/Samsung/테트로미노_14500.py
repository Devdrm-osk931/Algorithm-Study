import sys

n, m = tuple(map(int, sys.stdin.readline().split()))

grid = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

visited_pos = []
max_sum = 0


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def can_go(x, y):
    return in_range(x, y) and (x, y) not in visited_pos


def get_max_sum(cnt, sum_of_nums):
    if cnt == 4:
        global max_sum
        max_sum = max(max_sum, sum_of_nums)
        return

    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    for (x, y) in visited_pos:
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if can_go(new_x, new_y):
                visited_pos.append((new_x, new_y))
                get_max_sum(cnt + 1, sum_of_nums + grid[new_x][new_y])
                visited_pos.pop()


for i in range(n):
    for j in range(m):
        visited_pos.append((i, j))
        get_max_sum(1, grid[i][j])
        visited_pos.pop()

print(max_sum)