# BOJ 마법사 상어와 블리자드
# Samsung
BLANK = 0
answer = 0

n, m = tuple(map(int, input().split()))
shark_x, shark_y = n//2, n//2

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr = []  # grid를 1차원으로 핀 배열

cmds = [list(map(int, input().split())) for _ in range(m)]

# 상 하 좌 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

# l d r u
order = [2, 1, 3, 0]
distances = []
for dist in range(1, n):
    distances.append(dist)
    distances.append(dist)
distances.append(n-1)

tmp = [
    [0 for _ in range(n)]
    for _ in range(n)
]


def blizzard(direction, amount):
    curr_x, curr_y = n//2, n//2
    for _ in range(amount):
        curr_x, curr_y = curr_x + dxs[direction], curr_y + dys[direction]
        grid[curr_x][curr_y] = 0


def consecutive_check():
    global arr, answer
    consecutive_detected = False
    if arr:
        left_idx, right_idx, cnt = 0, 0, 1
        for idx in range(1, len(arr)):
            if arr[idx] == arr[left_idx]:
                cnt += 1
                right_idx = idx
            else:
                # left_idx ~ right_idx까지 지워줌
                # 터진 블록의 수, 갯수에 따라 점수 체크 로직 구현 필요
                if cnt >= 4:
                    # 폭발한 구슬의 숫자
                    marble_num = arr[left_idx]
                    answer += marble_num * cnt
                    consecutive_detected = True
                    for j in range(left_idx, right_idx + 1):
                        arr[j] = 0

                left_idx, right_idx, cnt = idx, idx, 1
        if cnt >= 4:
            marble_num = arr[left_idx]
            answer += marble_num * cnt
            consecutive_detected = True
            for j in range(left_idx, right_idx + 1):
                arr[j] = 0

        arr = [i for i in arr if i != 0]

    return consecutive_detected


def transform():
    global arr
    if not arr:
        return
    temp_arr = []
    left_idx, right_idx = 0, 0
    for idx in range(1, len(arr)):
        if arr[idx] == arr[left_idx]:
            right_idx = idx
        else:
            temp_arr += [right_idx - left_idx + 1, arr[left_idx]]
            left_idx, right_idx = idx, idx
    temp_arr += [right_idx - left_idx + 1, arr[left_idx]]

    # temp_arr 는 n * n 개 요소 중 상어 위치 제외 -> n * n - 1개의 요소가 최대임
    # 0 ~ n * n - 2
    if len(temp_arr) > n * n - 1:
        temp_arr = temp_arr[:n * n - 1]

    arr = temp_arr[:]


def move():
    temp = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    curr_x, curr_y, curr_idx, curr_dir = n // 2, n // 2, 0, 0
    for distance in distances:
        for _ in range(distance):
            curr_x, curr_y = curr_x + dxs[order[curr_dir]], curr_y + dys[order[curr_dir]]

            if curr_idx >= len(arr):
                for row in range(n):
                    for col in range(n):
                        grid[row][col] = temp[row][col]
                return

            temp[curr_x][curr_y] = arr[curr_idx]
            curr_idx += 1
        curr_dir = (curr_dir + 1) % 4


def compress_and_bomb():
    global arr
    # 1차원 배열로 옮긴다 -> 갯수는 n * n 개
    arr = []

    # grid를 순차적으로 보며 빈칸을 제외하고 arr에 넣어준다
    curr_x, curr_y, curr_dir = n // 2, n // 2, 0

    for distance in distances:
        for _ in range(distance):
            curr_x, curr_y = curr_x + dxs[order[curr_dir]], curr_y + dys[order[curr_dir]]
            if grid[curr_x][curr_y] == BLANK:
                continue
            arr.append(grid[curr_x][curr_y])
        curr_dir = (curr_dir + 1) % 4

    # arr 기준 4개 이상 연속한 숫자들을 가능한 많이 터트린다
    while True:
        removed = consecutive_check()
        if not removed:
            break

    # 변환
    transform()

    # arr를 2차원 격자에 반영해줌
    move()


def print_grid():
    print("After Blizzard")
    for row in grid:
        print(row)


def simulate():
    global answer
    for d, s in cmds:
        # 마법 시전 -> d 방향으로 s 거리 이내의 칸 파괴
        blizzard(d - 1, s)
        # 압축하고 터트리고 변환하고 옮기고
        compress_and_bomb()
        print_grid()
    print(answer)


simulate()
