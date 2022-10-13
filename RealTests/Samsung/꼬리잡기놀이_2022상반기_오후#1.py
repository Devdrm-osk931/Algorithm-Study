# Codetree 꼬리잡기놀이
# Samsung(2022상반기 오후#1)
n, m, k = tuple(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


# 머리부터 꼬리까지의 좌표를 순서대로 배열에 넣어 리턴
def detect_line(sx, sy):
    teammates = [(sx, sy)]

    x, y = sx, sy
    while a[x][y] != 3:
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny): continue
            if a[nx][ny] not in [2, 3]: continue
            if a[x][y] == 1 and a[nx][ny] == 3: continue
            if len(teammates) >= 2 and (nx, ny) == teammates[-2]:continue
            x, y = nx, ny
            break
        teammates.append((x, y))
    return teammates


def detect_whole_teams():
    teams = []
    # 1. 모든 머리를 찾고
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                teams.append(detect_line(i, j))
    return teams


def move_one_team(teammates):
    x, y = teammates[0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny):
            continue
        if a[nx][ny] not in [3, 4]:
            continue
        break

    # 현재 nx, ny에는 머리사람이 움직일 좌표가 저장이 되어있음
    next_coords = []
    for teammate in teammates:
        cx, cy = teammate
        next_coords.append((nx, ny))
        nx, ny = cx, cy
        a[cx][cy] = 4

    for idx, (x, y) in enumerate(next_coords, start=1):
        if idx == 1:
            a[x][y] = 1
        elif idx == len(next_coords):
            a[x][y] = 3
        else:
            a[x][y] = 2


def move_whole_team():
    # 1. 모든 팀을 우선 찾는다
    teams = detect_whole_teams()

    # 2. 각 팀에 대해 한칸씩 움직여준다
    for teammates in teams:
        move_one_team(teammates)


def throw_ball(round_num):
    round_num = round_num % (4 * n)

    if round_num < n:
        x1, y1 = round_num, 0
        x2, y2 = round_num, n
    elif round_num < 2 * n:
        x1, y1 = n - 1, round_num - n
        x2, y2 = -1, round_num - n
    elif round_num < 3 * n:
        x1, y1 = (3 * n - 1) - round_num, n - 1
        x2, y2 = (3 * n - 1) - round_num, -1
    else:
        x1, y1 = 0, (4 * n - 1) - round_num
        x2, y2 = n, (4 * n - 1) - round_num

    dx, dy = (x2 - x1) // n, (y2 - y1) // n

    x, y = x1, y1
    while (x, y) != (x2, y2):
        if a[x][y] not in [0, 4]:
            return (x, y)
        x, y = x + dx, y + dy
    return None


def calculate(coord):
    # 인자로 넘겨진 좌표가 존재하는 팀을 찾아야함
    teams = detect_whole_teams()
    for teammates in teams:
        for idx, teammate in enumerate(teammates, start=1):
            if teammate == coord:
                hx, hy = teammates[0]
                tx, ty = teammates[-1]
                a[hx][hy], a[tx][ty] = a[tx][ty], a[hx][hy]
                return idx * idx

# 틀
ans = 0
for round_num in range(k):
    move_whole_team()
    coord = throw_ball(round_num)
    if coord is None:
        continue
    ans += calculate(coord)
print(ans)
