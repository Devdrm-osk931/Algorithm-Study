n, m, k = tuple(map(int, input().split()))

virus = [
    [[] for _ in range(n)]
    for _ in range(n)
]

next_virus = [
    [[] for _ in range(n)]
    for _ in range(n)
]

food = [
    [0 for _ in range(n)]
    for _ in range(n)
]

next_food = [
    [0 for _ in range(n)]
    for _ in range(n)
]

delta = [
    list(map(int, input().split()))
    for _ in range(n)
]

dxs = [-1, -1, -1, 0, 0, 1, 1, 1]
dys = [-1, 0, 1, -1, 1, -1, 0, 1]


def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n


def breed(i, j):
    for dx, dy in zip(dxs, dys):
        nx = i + dx
        ny = j + dy

        if in_range(nx, ny):
            next_virus[nx][ny].append(1)


def simulate():
    # 옮기기 전용 배열 초기화
    for i in range(n):
        for j in range(n):
            next_food[i][j] = 0
            next_virus[i][j] = []

    # 바이러스 성장
    for i in range(n):
        for j in range(n):
            virus[i][j].sort()

            for age in virus[i][j]:
                if food[i][j] >= age:
                    food[i][j] -= age
                    next_virus[i][j].append(age + 1)
                else:
                    next_food[i][j] += age // 2

            next_food[i][j] += food[i][j]

    for i in range(n):
        for j in range(n):
            for age in next_virus[i][j]:
                if age % 5 == 0:
                    breed(i, j)

    for i in range(n):
        for j in range(n):
            next_food[i][j] += delta[i][j]

    for i in range(n):
        for j in range(n):
            virus[i][j] = next_virus[i][j][:]
            food[i][j] = next_food[i][j]

for _ in range(m):
    r, c, age = tuple(map(int, input().split()))
    r, c = r - 1, c - 1
    virus[r][c].append(age)

for i in range(n):
    for j in range(n):
        food[i][j] = 5

for _ in range(k):
    simulate()

ans = sum([
    len(virus[i][j])
    for i in range(n)
    for j in range(n)
])

print(ans)