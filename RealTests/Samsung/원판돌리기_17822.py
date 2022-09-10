# BOJ 원판돌리기 골드3
# Samsung

BLANK = 0
CW = 0
CCW = 1

n, m, t = tuple(map(int, input().split()))

temp = [0 for _ in range(m)]

plates = [
    list(map(int, input().split()))
    for _ in range(n)
]

removed = [
    [False for _ in range(m)]
    for _ in range(n)
]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def init_temp():
    for col in range(m):
        temp[col] = 0


def rotate(row, d, k):
    init_temp()

    if d == CW:
        for col in range(m):
            temp[(col + k) % m] = plates[row][col]

    elif d == CCW:
        for col in range(m):
            temp[(col - k) % m] = plates[row][col]

    for col in range(m):
        plates[row][col] = temp[col]


def num_exist():
    for i in range(n):
        for j in range(m):
            if plates[i][j] != BLANK:
                return True
    return False


def init_removed():
    for i in range(n):
        for j in range(m):
            removed[i][j] = False


def in_range(i, j):
    return 0 <= i < n and 0 <= j < m


def remove():
    is_removed = False
    # removed 배열을 초기화한다
    init_removed()

    # 삭제되지 않은 수가 있다면 인접한 상하좌우를 살피며 같은 숫자가 있는지 확인한다
    for i in range(n):
        for j in range(m):
            if plates[i][j] == BLANK:
                continue
            for dx, dy in zip(dxs, dys):
                ni, nj = i + dx, (j + dy) % m
                if in_range(ni, nj) and plates[ni][nj] == plates[i][j]:
                    removed[i][j] = removed[ni][nj] = True

    # 삭제된 숫자들을 0으로 반영한다
    for i in range(n):
        for j in range(m):
            if removed[i][j]:
                is_removed = True
                plates[i][j] = BLANK

    return is_removed


def process():
    num_sum = 0
    num_cnt = 0

    for i in range(n):
        for j in range(m):
            if plates[i][j] == BLANK:
                continue
            num_sum += plates[i][j]
            num_cnt += 1
    avg = num_sum / num_cnt

    for i in range(n):
        for j in range(m):
            if plates[i][j] == BLANK:
                continue
            if plates[i][j] > avg:
                plates[i][j] -= 1
            elif plates[i][j] < avg:
                plates[i][j] += 1


def simulate(x, d, k):
    # 원판의 행 중 x 의 배수인 행을 회전한다
    for row in range(x - 1, n, x):
        rotate(row, d, k)

    # 원판의 수가 남아있다면 인접하며 같은 수를 지운다
    if num_exist():
        is_removed = remove()
        if not is_removed:
            process()


# ============MAIN============
for _ in range(t):
    x, d, k = tuple(map(int, input().split()))
    simulate(x, d, k)

print(sum([
    plates[i][j]
    for i in range(n)
    for j in range(m)
    if plates[i][j] != BLANK
]))