# 격자크기, 박멸 진행 년수, 제초제 확산 범위, 제초제가 남아있는 년 수
n, m, k, c = tuple(map(int, input().split()))
answer = 0

# 상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# 격자
trees = [
    list(map(int, input().split()))
    for _ in range(n)
]

temp_trees = [
    [0 for _ in range(n)]
    for _ in range(n)
]

# 제초제 흔적
herb = [
    [0 for _ in range(n)]
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def grow_trees():
    for i in range(n):
        for j in range(n):
            # 나무가 없거나, 벽이라면 지나간다
            if not trees[i][j] or trees[i][j] == -1:
                continue

            adj = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                # 인접한 곳이 격자 내에 존재하고, 나무라면
                if in_range(nx, ny) and trees[nx][ny] > 0:
                    adj += 1

            trees[i][j] += adj


def copy_trees_to_temp():
    for i in range(n):
        for j in range(n):
            temp_trees[i][j] = trees[i][j]


def copy_to_trees():
    for i in range(n):
        for j in range(n):
            trees[i][j] = temp_trees[i][j]


def duplicate_trees():
    # temp_trees로 trees를 복사한다
    copy_trees_to_temp()

    # trees 격자 순회
    for i in range(n):
        for j in range(n):
            # 나무가 없거나 벽이면 지나간다
            if not trees[i][j] or trees[i][j] == -1:
                continue
            adj = 0
            plant = []
            # 나무가 있다면 상하 좌우를 살핀다
            for dx, dy in zip(dxs, dys):
                nx, ny = i + dx, j + dy
                if not in_range(nx, ny):
                    continue
                if trees[nx][ny] > 0 or trees[nx][ny] == -1 or herb[nx][ny]:
                    continue
                adj += 1
                plant.append((nx, ny))

            if adj > 0:
                amount = trees[i][j] // adj
                for x, y in plant:
                    temp_trees[x][y] += amount

    # temp_trees를 trees로 복사해준다
    copy_to_trees()


# 제초제를 뿌릴 최적의 위치를 찾는다
def herbicide(x, y):
    tree_kill = 0
    pos = []
    # 사선방향
    dxs = [-1, -1, 1, 1]
    dys = [-1, 1, -1, 1]

    cx, cy = x, y

    # 중앙 처리 -> 나무가 있다면 자르고 나무가 없다면(벽이거나) 해당 점까지만 처리하고(리턴한다)
    if not trees[cx][cy] or trees[cx][cy] == -1:
        pos.append((cx, cy))
        return tree_kill, pos

    else:
        pos.append((cx, cy))
        tree_kill += trees[cx][cy]

    for dx, dy in zip(dxs, dys):
        for amount in range(1, k + 1):
            nx, ny = cx + dx * amount, cy + dy * amount
            if not in_range(nx, ny):
                break
            if not trees[nx][ny] or trees[nx][ny] == -1:
                pos.append((nx, ny))
                break

            pos.append((nx, ny))
            tree_kill += trees[nx][ny]

    return tree_kill, pos


def get_best_pos():
    global answer
    best_cut = -1
    pos = []

    for i in range(n):
        for j in range(n):
            case_cut, case_pos = herbicide(i, j)
            if case_cut > best_cut:
                best_cut = case_cut
                pos = case_pos[:]

    # pos에 있는 나무 박멸, 0으로 처리
    answer += best_cut
    for i, j in pos:
        herb[i][j] = c + 1
        if trees[i][j] > 0:
            trees[i][j] = 0


def decrease():
    for i in range(n):
        for j in range(n):
            if herb[i][j] > 0:
                herb[i][j] -= 1


def simulate():
    for _ in range(m):
        # 1. 인접한 네 개의 칸 중 나무가 있는 칸의 수만큼 나무가 성장합니다. 성장은 모든 나무에게 동시에 일어난다
        grow_trees()
        # print("성장 이후")
        # for row in trees:
        #     print(row)
        # print()

        # 2. 나무 -> 인접한 4칸 중 벽/다른나무/제초제 없는 칸에 번식을 진행한다
        # 각 칸의 나무 그루 수에서 총 번식이 가능한 칸의 개수만큼 나누어진 그루 수만큼 번식, 동시에 발생
        duplicate_trees()
        # print("번식 이후")
        # for row in trees:
        #     print(row)
        # print()

        # 3. 제초제를 뿌렸을 때 나무가 가장 많이 박멸되는 칸에 제초제를 뿌린다
        # 4개의 대각선 방향으로 k칸 만큼 전파된다.
        # 전파되는 도중 벽/나무가 아예 없는 칸이 있는 경우 해당 칸 까지만 제초제가 뿌려지며 더 이상 전파되지 않는다
        # 제초제는 c년만큼 유지되다가 c + 1년째에 사라진다
        get_best_pos()
        # print("제초제 뿌린 이후")
        # for row in trees:
        #     print(row)
        # print()

        # 4. 제초제를 하나씩 감소시킨다
        decrease()
        # print("제초제 흔적")
        # for row in herb:
        #     print(row)
        #



simulate()
print(answer)