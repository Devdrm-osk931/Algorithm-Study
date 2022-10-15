# Import

# Global

# 마법 시전을 위한 dx/dy -> 상 하 좌 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


# Functions
# 마법을 시전한다 -> d방향으로 s개만큼 구슬 파괴로 시작
def destroy(d, s):
    cx, cy = N // 2, N // 2
    dx, dy = dxs[d], dys[d]

    for amount in range(1, s + 1):
        nx, ny = cx + dx * amount, cy + dy * amount
        grid[nx][ny] = 0


def matrix_to_list():
    global marbles
    cx, cy = N//2, N//2
    marbles = []
    for direction, cnt in zip(s_dir, s_dist):
        for _ in range(cnt):
            cx, cy = cx + dxs[direction], cy + dys[direction]
            if not grid[cx][cy]:
                continue
            marbles.append(grid[cx][cy])


def bomb():
    global score
    if not marbles:
        return False
    bombed = False

    target = marbles[0]
    cnt = 1
    for i in range(1, len(marbles)):
        if marbles[i] == marbles[i - 1]:
            cnt += 1
        else:
            if cnt >= 4:
                bombed = True
                # i - cnt  ... i - 1 까지 0으로 만든다
                score += target * cnt
                for j in range(i - cnt, i):
                    marbles[j] = 0
            target = marbles[i]
            cnt = 1
    if cnt >= 4:
        bombed = True
        score += target * cnt
        for j in range(len(marbles) - cnt, len(marbles)):
            marbles[j] = 0

    return bombed


def remove_zero():
    global marbles
    new = []
    for i in range(len(marbles)):
        if not marbles[i]:
            continue
        new.append(marbles[i])
    marbles = new[:]


def transform():
    global marbles
    if not marbles:
        return
    new = []
    target = marbles[0]
    cnt = 1

    for i in range(1, len(marbles)):
        if marbles[i] == marbles[i - 1]:
            cnt += 1
        else:
            new.append(cnt)
            new.append(target)
            target = marbles[i]
            cnt = 1
    new.append(cnt)
    new.append(target)

    if len(new) > N * N - 1:
        new = new[:N * N - 1]

    marbles = new[:]


def list_to_matrix():
    cx, cy = N // 2, N // 2
    idx = 0
    for direction, cnt in zip(s_dir, s_dist):
        for _ in range(cnt):
            cx, cy = cx + dxs[direction], cy + dys[direction]
            if idx > len(marbles) - 1:
                grid[cx][cy] = 0
            else:
                grid[cx][cy] = marbles[idx]
                idx += 1


def simulate(d, s):
    global marbles
    # 1. d 방향으로 s개만큼 구슬을 파괴한다
    destroy(d, s)

    # 2. 2차원 배열을 1차원 리스트로 전환하면서 압축한다
    matrix_to_list()

    # 3. 1차원 배열에 연속된 요소가 있다면 파괴한다
    while bomb():
        remove_zero()

    # 4. 변환한다
    transform()

    # 5. 변환한 값을 다시 2차원 배열에 반영한다
    list_to_matrix()


# Code
N, M = tuple(map(int, input().split()))  # 격자 크기, 마법 시전 횟수

# 달팽이 움직임
# 좌 하 우 상 * (N//2) + 좌
s_dir = []
s_dist = []

grid = [  # 격자
    list(map(int, input().split()))
    for _ in range(N)
]

marbles = []
score = 0

# 달팽이 움직임 정보를 만들어준다
for i in range(N//2):
    if i == N//2 - 1:
        s_dir += [2, 1, 3, 0, 2]
    else:
        s_dir += [2, 1, 3, 0]

for i in range(1, N):
    s_dist.append(i)
    s_dist.append(i)
    if i == N - 1:
        s_dist.append(i)

for _ in range(M):
    d, s = tuple(map(int, input().split()))
    simulate(d - 1, s)
print(score)
