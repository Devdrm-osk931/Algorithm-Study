# 변수 입력
n, m, curr_x, curr_y, cnt = tuple(map(int, input().split()))
DICE_FACES = 6

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

move_dirs = list(map(int, input().split()))

# 주사위 각 면에 쓰여진 값을 저장한다
# 위 앞 오 왼 위 아래 순서
dice = {
    'Top': 0,
    'Front': 0,
    'Right': 0,
    'Left': 0,
    'Back': 0,
    'Bottom': 0
}

# 동서남북 이동 방향을 설정한다
dxs, dys = [0, 0, 0, -1, 1], [0, 1, -1, 0, 0]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


# move_dir 방향으로 옮겼을때 주사위의 위치와 주사위의 각 면에 쓰여진 값을 갱신한다
def update(move_dir):
    top, front, right, left, back, bottom = dice.values()
    # 오른쪽으로 주사위를 굴린다
    if move_dir == 1:
        dice['Bottom'] = right
        dice['Top'] = left
        dice['Right'] = top
        dice['Left'] = bottom

    elif move_dir == 2:
        dice['Top'] = right
        dice['Bottom'] = left
        dice['Left'] = top
        dice['Right'] = bottom

    elif move_dir == 3:
        dice['Back'] = top
        dice['Top'] = front
        dice['Front'] = bottom
        dice['Bottom'] = back

    else:
        dice['Front'] = top
        dice['Bottom'] = front
        dice['Back'] = bottom
        dice['Top'] = back


def copy():
    # 주사위 밑면을 격자에 복사하고 주사위는 0으로 만든다
    if grid[curr_x][curr_y] == 0:
        grid[curr_x][curr_y] = dice['Bottom']


    else:
        dice['Bottom'] = grid[curr_x][curr_y]
        grid[curr_x][curr_y] = 0


def move_dice(move_dir):
    global curr_x, curr_y

    new_x, new_y = curr_x + dxs[move_dir], curr_y + dys[move_dir]

    # 격자의 바깥으로 이동하려는 시도인 경우 무시한다
    if in_range(new_x, new_y):
        # 유효한 움직임이라면 다음 위치를 갱신한다
        curr_x, curr_y = new_x, new_y
        update(move_dir)
        copy()
        print(dice['Top'])



def simulate():
    # 맨 처음 위치 처리
    copy()
    for move_dir in move_dirs:
        move_dice(move_dir)


simulate()
