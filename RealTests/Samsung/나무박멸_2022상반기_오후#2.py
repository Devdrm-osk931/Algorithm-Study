# Codetree 나무박멸
# Samsung 2022상반기 오후#2
BLANK = 0
WALL = -1
n, m, k, c = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
temp_tree = [[0 for _ in range(n)] for _ in range(n)]
die = [[0 for _ in range(n)] for _ in range(n)]
answer = 0

tdx = [-1, 0, 1, 0]
tdy = [0, -1, 0, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def grow_trees():
    for x in range(n):
        for y in range(n):
            cnt = 0
            if grid[x][y] == BLANK or grid[x][y] == WALL:
                continue

            for dx, dy in zip(tdx, tdy):
                nx, ny = x + dx, y + dy
                if in_range(nx, ny) and grid[nx][ny] > 0:
                    cnt += 1

            # cnt만큼 증가시켜준다
            grid[x][y] += cnt


# 나무를 동시에 성장시킨다
def expand_trees():
    # temp 배열 초기화
    for x in range(n):
        for y in range(n):
            temp_tree[x][y] = 0

    for x in range(n):
        for y in range(n):
            if grid[x][y] <= 0:
                continue

            cnt = 0
            for dx, dy in zip(tdx, tdy):
                nx, ny = x + dx, y + dy
                if not in_range(nx, ny):
                    continue
                if die[nx][ny]:
                    continue
                if grid[nx][ny] == 0:
                    cnt += 1

            for dx, dy in zip(tdx, tdy):
                nx, ny = x + dx, y + dy
                if not in_range(nx, ny):
                    continue
                if die[nx][ny]:
                    continue
                if grid[nx][ny] == 0:
                    temp_tree[nx][ny] += grid[x][y] // cnt

    for x in range(n):
        for y in range(n):
            grid[x][y] += temp_tree[x][y]


def find_pos():
    global answer

    dxs, dys = [-1, 1, 1, -1], [-1, -1, 1, 1]
    max_del, max_x, max_y = 0, 1, 1

    for x in range(n):
        for y in range(n):
            if grid[x][y] <= 0:
                continue

            cnt = grid[x][y]
            for dx, dy in zip(dxs, dys):
                nx, ny = x, y
                for _ in range(k):
                    nx, ny = nx + dx, ny + dy
                    if not in_range(nx, ny):
                        break
                    if grid[nx][ny] <= 0:
                        break
                    cnt += grid[nx][ny]

            if max_del < cnt:
                max_del = cnt
                max_x = x
                max_y = y
    answer += max_del

    if grid[max_x][max_y] > 0:
        grid[max_x][max_y] = 0
        die[max_x][max_y] = c + 1

    for dx, dy in zip(dxs, dys):
        nx, ny = max_x, max_y
        for _ in range(k):
            nx, ny = nx + dx, ny + dy
            if not in_range(nx, ny):
                break
            if grid[nx][ny] < 0:
                break
            if grid[nx][ny] == 0:
                die[nx][ny] = c + 1
                break
            grid[nx][ny] = 0
            die[nx][ny] = c + 1


def decrease():
    for x in range(n):
        for y in range(n):
            if die[x][y] > 0:
                die[x][y] -= 1

def simulate():
    for _ in range(m):
        #1. 나무성장
        grow_trees()

        #2. 나무번식
        expand_trees()

        #3. 제초제 뿌릴 위치 선정
        find_pos()

        #4. 제초제 1씩 감소
        decrease()
    print(answer)


simulate()