TAGGER = (-2, -2)
BLANK = (-1, -1)

n = 4

board = [
    [(0, 0) for _ in range(n)]
    for _ in range(n)
]

dxs = [-1, -1,  0,  1, 1, 1, 0, -1]
dys = [ 0, -1, -1, -1, 0, 1, 1,  1]

max_score = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def thief_can_go(x, y):
    return in_range(x, y) and board[x][y] != TAGGER


def tagger_can_go(x, y):
    return in_range(x, y) and board[x][y] != BLANK


def done(x, y, d):
    for dist in range(1, n + 1):
        nx, ny = x + dxs[d] * dist, y + dys[d] * dist
        if tagger_can_go(nx, ny):
            return False
    return True


def get_next(x, y, move_dir):
    for rotate_num in range(8):
        adjusted_dir = (move_dir + rotate_num) % 8
        nx, ny = x + dxs[adjusted_dir], y + dys[adjusted_dir]
        if thief_can_go(nx, ny):
            return (nx, ny, adjusted_dir)

    return (x, y, move_dir)


def swap(x, y, nx, ny):
    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]


def move(target_num):
    for x in range(n):
        for y in range(n):
            piece_num, move_dir = board[x][y]
            if piece_num == target_num:
                next_x, next_y, next_dir = get_next(x, y, move_dir)
                board[x][y] = (piece_num, next_dir)
                swap(x, y, next_x, next_y)
                return


def move_all():
    for i in range(1, n * n + 1):
        move(i)


def search_max_score(x, y, d, score):
    global max_score

    if done(x, y, d):
        max_score = max(max_score, score)
        return

    for dist in range(1, n + 1):
        nx, ny = x + dxs[d] * dist, y + dys[d] * dist
        if not tagger_can_go(nx, ny):
            continue

        temp = [
            [board[i][j] for j in range(n)]
            for i in range(n)
        ]

        extra_score, next_dir = board[nx][ny]
        board[x][y] = BLANK
        board[nx][ny] = TAGGER
        move_all()

        search_max_score(nx, ny, next_dir, score + extra_score)

        for i in range(n):
            for j in range(n):
                board[i][j] = temp[i][j]


for i in range(n):
    given_row = list(map(int, input().split()))
    for j in range(n):
        p, d = given_row[j * 2], given_row[j * 2 + 1]
        board[i][j] = (p, d - 1)

# 처음 (0, 0) 도둑말을 잡고, 모든 도둑말이 이동한 다음에 시작합니다.
init_score, init_dir = board[0][0]
board[0][0] = TAGGER

move_all()

search_max_score(0, 0, init_dir, init_score)
print(max_score)