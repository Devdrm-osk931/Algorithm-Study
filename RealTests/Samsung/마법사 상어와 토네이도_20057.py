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


def add_sand(x, y, amount):
    global out_sand

    if in_range(x, y):
        sand[x][y] += amount
    else:
        out_sand += amount


def end():
    return not curr_x and not curr_y


def move():
    global curr_x, curr_y, curr_dir

    for move_cnt in move_cnts:
        for _ in range(move_cnt):
            prev_x, prev_y = curr_x, curr_y
            curr_x, curr_y = prev_x + dxs[curr_dir], prev_y + dys[curr_dir]
            total = sand[curr_x][curr_y]
            flied = 0

            for dx, dy, percent in patterns[curr_dir]:
                a, b = prev_x + dx, prev_y + dy
                fly = total * percent // 100
                add_sand(a, b, fly)
                flied += fly

            # a% 위치에 대해 처리
            a_x, a_y = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]
            add_sand(a_x, a_y, total - flied)
            sand[curr_x][curr_y] = 0

        curr_dir = (curr_dir + 1) % 4


# logic
curr_x, curr_y = N//2, N//2
curr_dir = 0
move()
print(out_sand)