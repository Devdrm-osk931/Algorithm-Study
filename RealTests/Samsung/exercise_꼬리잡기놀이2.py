# 전역
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
#함수부
def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def find_a_team(i, j, route, person):
    visited[i][j] = True
    route.append((i, j))
    person.append(grid[i][j])
    for dx, dy in zip(dxs, dys):
        nx, ny = i + dx, j + dy

        if not in_range(nx, ny):
            continue

        if visited[nx][ny]:
            continue

        if grid[i][j] == 1:
            if grid[nx][ny] == 2:
                i, j = nx, ny
                find_a_team(nx, ny, route, person)
                break
        elif grid[i][j] == 2:
            if grid[nx][ny] in [2, 3]:
                i, j = nx, ny
                find_a_team(nx, ny, route, person)
                break
        elif grid[i][j] == 3:
            if grid[nx][ny] == 4:
                i, j = nx, ny
                find_a_team(nx, ny, route, person)
                break
        else:
            if grid[nx][ny] == 4:
                i, j = nx, ny
                find_a_team(nx, ny, route, person)
                break
    return route, person


def find_all_teams():
    teams = []
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                print(find_a_team(i, j, [], []))

def move_all_teams():
    teams = find_all_teams()

    for team in teams:
        move_a_team(team)

#코드부
# 격자크기, 팀의 갯수, 라운드 수
n, m, k = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

visited = [
    [False for _ in range(n)]
    for _ in range(n)
]

catch = 0
#
# for round in range(m):
#     move_all_teams()
#     catch = throw_ball(round)
#     if not catch:
#         continue
#     score += calculate(catch)

print(find_all_teams())
route_arr = [
    [0 for _ in range(n)]
    for _ in range(n)
]



# 7 2 1
# 2 2 1 0 0 0 0
# 2 0 3 0 2 1 4
# 2 2 2 0 2 0 4
# 0 0 0 0 3 0 4
# 0 0 4 4 4 0 4
# 0 0 4 0 0 0 4
# 0 0 4 4 4 4 4


