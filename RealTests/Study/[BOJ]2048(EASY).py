# BOJ 12100 2048(Easy)
# Samsung Gold2
LIMIT = 5
answer = 0
N = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(N)
]

copied = [
    row[:]
    for row in grid
]

next_grid = [
    [0 for _ in range(N)]
    for _ in range(N)
]


cmds = ['U', 'D', 'R', 'L']
selected = []


def init_next_grid():
    for row in range(N):
        for col in range(N):
            next_grid[row][col] = 0


def init_grid():
    for row in range(N):
        for col in range(N):
            grid[row][col] = copied[row][col]


def drop():
    init_next_grid()

    for col in range(N):
        prev = -1
        next_row = N - 1
        for row in range(N - 1, -1, -1):
            if grid[row][col] == 0:
                continue

            if prev == -1:
                prev = grid[row][col]

            else:
                if grid[row][col] == prev:
                    next_grid[next_row][col] = prev * 2
                    prev = -1
                    next_row -= 1

                else:
                    next_grid[next_row][col] = prev
                    next_row -= 1
                    prev = grid[row][col]

        if prev != -1:
            next_grid[next_row][col] = prev

    for row in range(N):
        for col in range(N):
            grid[row][col] = next_grid[row][col]


def rotate_right():
    init_next_grid()

    """
    123      741
    456  ->  852
    789      963
    
    0,0 -> 2, 0
    0,1 -> 1, 0
    0,2 -> 0, 0
    """

    for row in range(N):
        for col in range(N):
            next_grid[row][col] = grid[N - 1 - col][row]

    for row in range(N):
        for col in range(N):
            grid[row][col] = next_grid[row][col]


def rotate_left():
    init_next_grid()
    """
    123      369
    456  ->  258
    789      147
    
    0,0 -> 0, 2
    0,1 -> 1, 2
    0,2 -> 2, 2
    """

    for row in range(N):
        for col in range(N):
            next_grid[row][col] = grid[col][N - 1 - row]

    for row in range(N):
        for col in range(N):
            grid[row][col] = next_grid[row][col]


# 블록들을 위로
def up():
    for _ in range(2):
        rotate_right()
    drop()
    for _ in range(2):
        rotate_right()


def down():
    drop()


def right():
    rotate_right()
    drop()
    rotate_left()


def left():
    rotate_left()
    drop()
    rotate_right()


cmd_map = {
    'U': up,
    'D': down,
    'R': right,
    'L': left
}


def backtracking(cnt):
    global grid, answer
    if cnt == LIMIT:
        init_grid()
        for cmd in selected:
            cmd_map[cmd]()

        answer = max(answer, max(grid[i][j] for i in range(N) for j in range(N)))

        return

    for cmd in cmds:
        selected.append(cmd)
        backtracking(cnt + 1)
        selected.pop()

backtracking(0)
print(answer)