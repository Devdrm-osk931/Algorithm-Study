# BOJ 드래곤커브
# Samsung

# 방향: 우, 상, 좌, 하 -> 0, 1, 2, 3
# 0세대: 오른쪽
# 1세대: 오른쪽, 상
# 2세대: 오른쪽, 상 / 좌, 상
# 3세대: 우 상 좌 상 / 좌 하 좌 상
# 4세대: 우 상 좌 상 좌 하 좌 상 / 좌 하 우 하 좌 하 좌 상

"""
방향 변화 관계
상 -> 좌
하 -> 우
좌 -> 하
우 -> 상
이전 배열 거꾸로 해서 방향 + 1
"""

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

# 0 <= x <= 100
grid = [
    [0 for _ in range(101)]
    for _ in range(101)
]


def process(dir):
    return (dir + 1) % 4


def dragon_curve(x, y, d, g):
    curr_x, curr_y = x, y
    # 처음 위치
    grid[curr_x][curr_y] = 1

    # 방향 배열
    dirs = [d]

    for _ in range(g):
        tmp = dirs[::-1]
        for idx in range(len(tmp)):
            tmp[idx] = (tmp[idx] + 1) % 4
        dirs += tmp

    for dir in dirs:
        dx, dy = dxs[dir], dys[dir]
        nx, ny = curr_x + dx, curr_y + dy
        grid[nx][ny] = 1
        curr_x, curr_y = nx, ny


n = int(input())
answer = 0
for _ in range(n):
    x, y, d, g = tuple(map(int, input().split()))
    dragon_curve(x, y, d, g)

for i in range(100):
    for j in range(100):
        if not grid[i][j]:
            continue

        if grid[i + 1][j] and grid[i][j + 1] and grid[i + 1][j + 1]:
            answer += 1

print(answer)