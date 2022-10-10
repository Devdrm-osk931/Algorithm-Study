n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
arr = []
cmd = [
    list(map(int, input().split()))
    for _ in range(m)
]

# 최종점수
score = 0

# 상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


# grid에서 중심을 기준으로 d방향으로 s만큼 이내에 있는 구슬을 0으로 만든다
def destroy(d, s):
    cx, cy = n//2, n//2
    for _ in range(s):
        cx, cy = cx + dxs[d], cy + dys[d]
        grid[cx][cy] = 0


# 격자를 중심부터 나선형으로 돌면서 격자를 탐색하여 0이 아닌 수를 arr에 넣어준다
def grid_to_arr():
    global arr
    arr = []  # arr 초기화
    # 좌 하 우 상
    ddx = [0, 1, 0, -1]
    ddy = [-1, 0, 1, 0]

    cx, cy = n//2, n//2
    curr_dir = 0
    cnt = 2

    for dist in range(1, n):
        if dist == n - 1:
            cnt += 1
        for _ in range(cnt):
            for _ in range(dist):
                cx, cy = cx + ddx[curr_dir], cy + ddy[curr_dir]
                if grid[cx][cy] == 0:
                    continue
                arr.append(grid[cx][cy])
            curr_dir = (curr_dir + 1) % 4


# arr를 탐색하며 공통된 요소의 갯수에 따라 0으로 바꾸고 점수를 획득한다
def bomb():
    if not arr:
        return 0
    global score
    lower, cnt = 0, 1
    point = 0
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            cnt += 1
        else:
            # i - cnt   ...   i - 1  i
            if cnt >= 4:
                for j in range(lower, i):
                    point += arr[j]
                    arr[j] = 0
            lower, cnt = i, 1
    # 루프 종료 시 동일요소 처리가 되지 않고 빠져나왔을 수 있음
    if cnt >= 4:
        for j in range(lower, len(arr)):
            point += arr[j]
            arr[j] = 0

    score += point
    return point


def remove_zero():
    global arr
    temp = []
    for elem in arr:
        if elem:
            temp.append(elem)
    arr = temp[:]


def expand():
    global arr
    if not arr:
        return 0
    temp = []
    cnt = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            cnt += 1
        else:
            temp.append(cnt)
            temp.append(arr[i - 1])
            cnt = 1

    # 마지막 요소 처리
    temp.append(cnt)
    temp.append(arr[-1])

    # arr길이의 최대값은 -> n**2 - 1 -> 최대 인덱스 --> n ** 2 - 2
    if len(temp) > n * n - 1:
        arr = temp[:n*n - 1]
    else:
        arr = temp[:]


def arr_to_grid():
    # 좌 하 우 상
    ddx = [0, 1, 0, -1]
    ddy = [-1, 0, 1, 0]

    cx, cy = n // 2, n // 2
    curr_dir = 0
    cnt = 2
    idx = 0

    for dist in range(1, n):
        if dist == n - 1:
            cnt += 1
        for _ in range(cnt):
            for _ in range(dist):
                cx, cy = cx + ddx[curr_dir], cy + ddy[curr_dir]
                if idx < len(arr):
                    grid[cx][cy] = arr[idx]
                    idx += 1
                else:
                    grid[cx][cy] = 0
            curr_dir = (curr_dir + 1) % 4


def simulate():
    for d, s in cmd:
        # 1. d 방향으로 s 이내에 있는 구슬 파괴
        destroy(d - 1, s)

        # 2. 격자를 1차원 리스트로 옮기면서 빈칸을 압축한다
        grid_to_arr()

        # 3. 4개 이상 동일한 구슬이 있다면 폭발 -> 점수 획득
        while bomb():
            remove_zero()

        # 4. 구슬 확대
        expand()

        # 5. 1차원 리스트를 2차원 리스트로 옮김
        arr_to_grid()

    print(score)

simulate()