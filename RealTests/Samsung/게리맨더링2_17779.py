import sys

INT_MAX = sys.maxsize

# 변수 선언 및 입력:

n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

border = [
    [False for _ in range(n)]
    for _ in range(n)
]

total_sum = 0


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


# 가장 아래 지점을 제외한 3개의 꼭지점이 전부
# 격자 안에 들어오는 경우에만 해당 직사각형을 그릴 수 있습니다.
def possible_to_draw(x, y, k, l):
    return in_range(x - k, y + k) and in_range(x - k - l, y + k - l) \
           and in_range(x - l, y - l)


def draw_slanted_rect_border(x, y, k, l):
    dxs, dys = [-1, -1, 1, 1], [1, -1, -1, 1]
    move_nums = [k, l, k, l]

    # 먼저 border값을 전부 false로 초기화합니다.
    for i in range(n):
        for j in range(n):
            border[i][j] = False

    # 기울어진 직사각형의 경계를 쭉 따라가봅니다.
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x, y = x + dx, y + dy
            border[x][y] = True


def get_score(x, y, k, l):
    population = [0, 0, 0, 0, 0]

    # 경계를 표시합니다.
    draw_slanted_rect_border(x, y, k, l)

    # 좌측 상단 구역
    for i in range(x - l):
        for j in range(y + k - l + 1):
            if border[i][j]:
                break

            population[0] += grid[i][j]

    # 좌측 하단 구역
    for i in range(x - l, n):
        for j in range(y):
            if border[i][j]:
                break

            population[1] += grid[i][j]

    # 우측 상단 구역
    for i in range(x - k + 1):
        for j in range(n - 1, y + k - l, -1):
            if border[i][j]:
                break

            population[2] += grid[i][j]

    # 우측 하단 구역
    for i in range(x - k + 1, n):
        for j in range(n - 1, y - 1, -1):
            if border[i][j]:
                break

            population[3] += grid[i][j]

    population[4] = total_sum - sum(population[:4])
    return max(population) - min(population)


total_sum = sum([
    grid[i][j]
    for i in range(n)
    for j in range(n)
])

ans = INT_MAX

# (i, j)를 시작으로 1, 2, 3, 4 방향
# 순서대로 길이 [k, l, k, l] 만큼 이동하면 그려지는
# 기울어진 직사각형을 잡아보는
# 완전탐색을 진행해봅니다.
for i in range(n):
    for j in range(n):
        for k in range(1, n):
            for l in range(1, n):
                # 직사각형을 그릴 수 있는 경우에만
                # 답을 갱신합니다.
                if possible_to_draw(i, j, k, l):
                    ans = min(ans, get_score(i, j, k, l))

print(ans)