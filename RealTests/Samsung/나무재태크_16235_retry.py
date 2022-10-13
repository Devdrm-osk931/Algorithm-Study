# 나무재태크 복습

n, m, k = tuple(map(int, input().split()))

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

trees = [
    [[] for _ in range(n)]
    for _ in range(n)
]

temp_trees = [
    [[] for _ in range(n)]
    for _ in range(n)
]

nutrition = [
    [5 for _ in range(n)]
    for _ in range(n)
]

for _ in range(m):
    x, y, t = tuple(map(int, input().split()))
    trees[x - 1][y - 1].append(t)

# 8개 방향에 대한 dxs/dys
dxs = [-1, -1, -1, 0, 0, 1, 1, 1]
dys = [-1, 0, 1, -1, 1, -1, 0, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def spring():
    dead = []
    # temp_trees 를 초기화 해준다
    for x in range(n):
        for y in range(n):
            temp_trees[x][y] = []

    for x in range(n):
        for y in range(n):
            if not trees[x][y]:  # 격자에 나무가 없는 곳은 지나간다
                continue

            trees[x][y].sort()  # 격자에 나무가 있다면 나이의 오름차순으로 정렬을 수행한다
            # 각 나무의 나이를 살펴본다
            for tree_age in trees[x][y]:
                # 나무의 나이만큼 영양분이 있는 경우 나무는 자랄 수 있다
                if nutrition[x][y] >= tree_age:
                    temp_trees[x][y].append(tree_age + 1)
                    nutrition[x][y] -= tree_age

                # 영양소가 부족한 경우 나무가 죽어 영양분이 된다
                else:
                    dead.append((x, y, tree_age//2))

    # temp_trees 를 반영해준다
    for x in range(n):
        for y in range(n):
            trees[x][y] = temp_trees[x][y]

    return dead


def summer(dead):
    for x, y, amount in dead:
        nutrition[x][y] += amount


def fall():
    # temp_tree 배열 초기화
    for x in range(n):
        for y in range(n):
            temp_trees[x][y] = []


    # trees를 순회하며 나무의 나이가 5의 배수인 것이 있는지 확인한다
    for x in range(n):
        for y in range(n):
            if not trees[x][y]:
                continue

            for tree_age in trees[x][y]:
                # 기존에 있던 나무를 temp로 옮겨준다
                temp_trees[x][y].append(tree_age)
                # 해당 나무의 나이가 5의 배수라면 번식을 한다
                if tree_age % 5 == 0:
                    cx, cy = x, y
                    for dx, dy in zip(dxs, dys):
                        nx, ny = cx + dx, cy + dy
                        # 범위 안에 있다면 해당 방향에 나이가 1인 나무를 심어준다
                        if in_range(nx, ny):
                            temp_trees[nx][ny].append(1)

    # temp_trees 를 반영해준다
    for x in range(n):
        for y in range(n):
            trees[x][y] = temp_trees[x][y]


# 양분을 추가한다
def winter():
    for x in range(n):
        for y in range(n):
            nutrition[x][y] += a[x][y]


def get_trees():
    answer = 0
    for x in range(n):
        for y in range(n):
            if not trees[x][y]:
                continue
            answer += len(trees[x][y])
    print(answer)


def simulate():
    for _ in range(k):
        # 1. 봄: 나무가 자신의 나이만큼 양분을 먹고 나이가 1 증가한다, 양분이 없다며 그 나무는 죽게 된다
        dead = spring()

        # 2. 여름: 죽은 나무가 양분으로 변하게 된다, 죽은 나무의 나이 / 2 값이 양분으로 추가된다
        summer(dead)

        # 3. 가을: 나무가 번식한다; 나무의 나이가 5의 배수인것에 한해 인접한 8개의 방향으로 나이 1인 나무가 생긴다, 벗어나는 칸 X
        fall()

        # 4. a 격자만큼 양분이 추가된다
        winter()

    # 5. k년 이후 살아남은 나무의 수를 구한다
    get_trees()


simulate()