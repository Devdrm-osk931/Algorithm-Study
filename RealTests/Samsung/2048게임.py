n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
save = [row[:] for row in grid]
temp = [[0 for _ in range(n)] for _ in range(n)]
ans = 0
move_dirs = [0] * 5

# Get Max Element
def get_max():
    return max([
        grid[i][j]
        for i in range(n)
        for j in range(n)
    ])

# Init array
def init(array):
    for i in range(n):
        for j in range(n):
            array[i][j] = 0


# Copy array to grid
def copy(array):
    for i in range(n):
        for j in range(n):
            grid[i][j] = array[i][j]


# Rotation Logic
def rotate():
    init(temp)

    for i in range(n):
        for j in range(n):
            temp[i][j] = grid[n - j - 1][i]

    copy(temp)


# Drop Logic
def drop():
    init(temp)

    for j in range(n):
        keep, next_row = -1, n - 1

        for i in range(n - 1, -1, -1):
            if not grid[i][j]:
                continue

            # 이전에 관찰된 숫자가 없는 경우
            if keep == -1:
                keep = grid[i][j]

            # 이전에 관찰된 숫자와 지금 관찰된 숫자가 다른 경우 이전에 관찰된 숫자를 떨어트린다
            elif keep != grid[i][j]:
                temp[next_row][j] = keep
                next_row -= 1
                keep = grid[i][j]

            else:
                temp[next_row][j] = keep * 2
                keep = -1
                next_row -= 1

        if keep != -1:
            temp[next_row][j] = keep
            next_row -= 1
    copy(temp)

# Moving Numbers to certain direction --> Rotate & Drop
def move(move_dir):
    for _ in range(move_dir):
        rotate()
    drop()
    for _ in range(4 - move_dir):
        rotate()


# Simulate and get maximum number for one case
def simulate():
    global ans
    # 초기 상태로 진행해야한다
    copy(save)

    for move_dir in move_dirs:
        move(move_dir)

    ans = max(ans, get_max())


def solve(cnt):
    if cnt == 5:
        simulate()
        return
    for dir in range(4):
        move_dirs[cnt] = dir
        solve(cnt + 1)


def print_array(array):
    for row in array:
        for elem in row:
            print(elem, end=' ')
        print()


solve(0)
print(ans)