# 전역변수
dxs, dys = [-1, 0, 1, 0], [0, -1, 0, 1]


# 함수
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def find_team(i, j):
    x, y = i, j
    team = [(x, y)]

    while grid[x][y] != 3:
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if not in_range(nx, ny):
                continue
            if grid[nx][ny] not in [2, 3]:
                continue
            if grid[x][y] == 1 and grid[nx][ny] == 3:
                continue
            if len(team) > 2 and team[-2] == (nx, ny):
                continue
            x, y = nx, ny
            break
        team.append((x, y))

    return team


def find_all_teams():
    teams = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                teams.append(find_team(i, j))

    return teams


def move(team):
    x, y = team[0]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if not in_range(nx, ny):
            continue
        if grid[nx][ny] not in [3, 4]:
            continue
        break

    next_pos = []
    for teammate in team:
        cx, cy = teammate
        next_pos.append((nx, ny))
        grid[cx][cy] = 4
        nx, ny = cx, cy

    for i, (x, y) in enumerate(next_pos, start=1):
        if i == 1:
            grid[x][y] = 1
        elif i == len(next_pos):
            grid[x][y] = 3
        else:
            grid[x][y] = 2


def move_all_teams():
    teams = find_all_teams()
    for team in teams:
        move(team)


def throw_ball(round):
    round %= 4 * n
    dir, x, y = -1, -1, -1
    if 0 <= round < n:
        dir = (0, 1)
        x, y = round, 0

    elif n <= round < 2 * n:
        dir = (-1, 0)
        x, y = n - 1, round - n


    elif 2 * n <= round < 3 * n:
        dir = (0, -1)
        x, y = 3 * n - 1 - round, n - 1

    else:
        dir = (1, 0)
        x, y = 0, 4 * n - 1 - round

    for amount in range(n):
        nx, ny = x + dir[0] * amount, y + dir[1] * amount
        if grid[nx][ny] in [1, 2, 3]:
            return nx, ny

    return None


def add_score(catch_coordinate):
    global score
    teams = find_all_teams()
    for team in teams:
        for i, teammate in enumerate(team, start=1):
            if teammate == catch_coordinate:
                score += i * i
                headx, heady = team[0]
                tailx, taily = team[-1]
                grid[headx][heady], grid[tailx][taily] = grid[tailx][taily], grid[headx][heady]
                return

# 코드
# 격자의 크기, 팀의 개수, 라운드 수
n, m, k = tuple(map(int, input().split()))
score = 0
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# k번의 라운드동안 진행
for round in range(k):
    # 1. 모든 팀을 머리사람부터 한칸씩 움직인다
    move_all_teams()

    # 2. 공을 던진다
    catch_coordinate = throw_ball(round)
    if catch_coordinate is not None:
        # 3. 점수를 획득한다
        add_score(catch_coordinate)

print(score)
