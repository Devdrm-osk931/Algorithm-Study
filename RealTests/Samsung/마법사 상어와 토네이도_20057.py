# BOJ 20057 골드3
# Samsung

N = int(input())

sand = [
    list(map(int, input().split()))
    for _ in range(N)
]

out_sand = 0


# 1 1 2 2 3 3 4 4 5 5 6 6 (7 - 1)
# l d r u l d r u l d r u l

move_cnts = []
for i in range(1, N):
    move_cnts.append(i)
    move_cnts.append(i)
move_cnts.append(N - 1)

# l d r u
dxs = [0, 1, 0, -1]
dys = [-1, 0, 1, 0]

# x -> y 로 갈 때 퍼지는 패턴
patterns = [
    [(-1, 0, 1), (1, 0, 1), (-1, -1, 7), (1, -1, 7), (-2, -1, 2), (2, -1, 2), (-1, -2, 10), (1, -2, 10), (0, -3, 5)],
    [(0, -1, 1), (0, 1, 1), (1, -1, 7), (1, 1, 7), (1, -2, 2), (1, 2, 2), (2, -1, 10), (2, 1, 10), (3, 0, 5)],
    [(-1, 0, 1), (1, 0, 1), (-1, 1, 7), (1, 1, 7), (-2, 1, 2), (2, 1, 2), (-1, 2, 10), (1, 2, 10), (0, 3, 5)],
    [(0, -1, 1), (0, 1, 1), (-1, -1, 7), (-1, 1, 7), (-1, -2, 2), (-1, 2, 2), (-2, -1, 10), (-2, 1, 10), (-3, 0, 5)]
]

"""
달팽이 움직임 로직!
curr_dir = 0
index = 1
curr_x, curr_y = N//2, N//2
tmp[curr_x][curr_y] = index
index += 1


for move_cnt in move_cnts:
    for _ in range(move_cnt):
        curr_x, curr_y = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]
        tmp[curr_x][curr_y] = index
        index += 1
    curr_dir = (curr_dir + 1) % 4
"""


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


x, y = N//2, N//2
dir_num = 0
for move_cnt in move_cnts:
    for _ in range(move_cnt):
        nx, ny = x + dxs[dir_num], y + dys[dir_num]

        original = sand[nx][ny]
        total = sand[nx][ny]
        for dx, dy, percent in patterns[dir_num]:
            fx, fy = x + dx, y + dy
            amount = original * percent // 100

            # 날아가는 곳이 격자 안에 있는 경우
            if in_range(fx, fy):
                sand[fx][fy] += amount
            else:
                out_sand += amount

            total -= amount

        ax, ay = nx + dxs[dir_num], ny + dys[dir_num]

        # a 만큼 날아가는 곳이 격자 안에 있는 경우
        if in_range(ax, ay):
            sand[ax][ay] = total
        else:
            out_sand += total

        # nx, ny 자리에 있는 모래를 없앤다
        sand[nx][ny] = 0
        x, y = nx, ny

    dir_num = (dir_num + 1) % 4

print(out_sand)