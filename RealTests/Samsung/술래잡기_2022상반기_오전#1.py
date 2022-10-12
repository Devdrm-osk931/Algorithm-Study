# Codetree 술래잡기
# Samsung(2022 상반기 오전#1)
# https://www.codetree.ai/frequent-problems/hide-and-seek/description

# 상 우 하 좌
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# 1: 좌우(우)  2: 상하(하)
# 우 하 상 좌
d_dxs = [0, 1, -1, 0]
d_dys = [1, 0, 0, -1]

# INPUT
n, m, h, k = tuple(map(int, input().split()))

dlist = [
    [[] for _ in range(n)]
    for _ in range(n)
]

temp = [
    [[] for _ in range(n)]
    for _ in range(n)
]

tree = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 도망자 정보: direction => 1:우  2: 하
for _ in range(m):
    x, y, direction = tuple(map(int, input().split()))
    dlist[x - 1][y - 1].append(direction - 1)

for _ in range(h):
    r, c = tuple(map(int, input().split()))
    tree[r - 1][c - 1] = 1


# 달팽이 움직임 관련 정보
snail_dir = []
snail_go = [0, 1, 2, 3]
snail_back = [2, 1, 0, 3]
for _ in range(n//2):
    snail_dir += snail_go
snail_dir.append(snail_dir[0])
for _ in range(n//2):
    snail_dir += snail_back
snail_dir.append(snail_back[0])

snail_dist = []
cnt = 2
for d in range(1, n):
    if d == n - 1:
        cnt += 1
    for _ in range(cnt):
        snail_dist.append(d)
snail_dist += snail_dist[::-1]
all_dir = []
for curr_dir, curr_dist in zip(snail_dir, snail_dist):
    for _ in range(curr_dist):
        all_dir.append(curr_dir)

# 술래 정보
cx, cy = n//2, n//2
curr_vision = all_dir[0]
score = 0

# # 현재 술래의 위치와 보고있는 방향을 트래킹할 수 있음
# print("grid")
# print(f"현재위치: {cx}, {cy}, 현재 방향: {all_dir[0]}")
# for row in check:
#     print(row)
# for i in range(len(all_dir)):
#     check[cx][cy] = 0
#     cx, cy = cx + dxs[all_dir[i]], cy + dys[all_dir[i]]
#     check[cx][cy] = 1
#     print(f"현재위치: {cx}, {cy}, 현재 방향: {all_dir[(i + 1) % len(all_dir)]}")
#     for row in check:
#         print(row)


# 격자 내에 존재하는 점인지 확인
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 도망자가 갈 수 있는 점인지 확인
def can_go(x, y):
    return in_range(x, y) and (x, y) != (cx, cy)


def init_temp():
    for x in range(n):
        for y in range(n):
            temp[x][y] = []


def move_all_d():
    init_temp()
    for x in range(n):
        for y in range(n):
            # 해당 위치에 아무것도 없다면 지나친다
            if not dlist[x][y]:
                continue

            # 해당 위치가 술래로부터 거리가 3보다 크다면 움직이지 않는다
            if abs(x - cx) + abs(y - cy) > 3:
                for d in dlist[x][y]:
                    temp[x][y].append(d)

            # 움직여야하는 술래들의 경우
            else:
                for d in dlist[x][y]:
                    nx, ny = x + d_dxs[d], y + d_dys[d]
                    # 격자를 벗어난다면 방향을 반대로 살펴본다
                    if not in_range(nx, ny):
                        d = 3 - d
                        nx, ny = x + d_dxs[d], y + d_dys[d]
                    # 바라보는 위치에 술래가 없다면 이동
                    if (nx, ny) != (cx, cy):
                        temp[nx][ny].append(d)
                    else:
                        temp[x][y].append(d)

    # temp를 dlist에 반영
    for x in range(n):
        for y in range(n):
            dlist[x][y] = temp[x][y]


def move_tagger(turn):
    global cx, cy, curr_vision
    idx = turn % len(all_dir)
    cx, cy = cx + dxs[all_dir[idx]], cy + dys[all_dir[idx]]
    curr_vision = all_dir[(idx + 1) % len(all_dir)]


def catch():
    catched = 0
    curr_x, curr_y, curr_v = cx, cy, curr_vision

    for delta in range(3):
        nx, ny = curr_x + dxs[curr_v] * delta, curr_y + dys[curr_v] * delta
        if not in_range(nx, ny) or not dlist[nx][ny]:
            continue
        if dlist[nx][ny]:
            if not tree[nx][ny]:
                catched += len(dlist[nx][ny])
                while dlist[nx][ny]:
                    dlist[nx][ny].pop()
    return catched


def simulate():
    global score
    for turn in range(k):
        # 1. 도망자를 움직인다
        move_all_d()

        # 2. 술래를 한칸 움직인다
        move_tagger(turn)

        # 3. 술래가 현재 보고있는 시야를 기준으로 술래를 잡는다
        cnt = catch()

        # 4. 현재 턴에 대한 점수를 계산한다
        score += (turn + 1) * cnt
    print(score)


simulate()