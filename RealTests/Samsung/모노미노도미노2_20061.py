N = 10
types = [
    [(0, 0)],
    [(0, 0), (0, 1)],
    [(0, 0), (1, 0)]
]

locations = []


# 게임을 진행할 10x10 격자 선언
board = [
    [False for _ in range(N)]
    for _ in range(N)
]

# 블록이 낙하한 후 상태
next_board = [
    [False for _ in range(N)]
    for _ in range(N)
]


def copy():
    for i in range(N):
        for j in range(N):
            board[i][j] = next_board[i][j]


def init():
    for i in range(N):
        for j in range(N):
            next_board[i][j] = board[i][j]


def remove():
    global locations
    for x, y in locations:
        board[x][y] = False
    locations = []


def drop_down(t):
    max_row = -1
    # 각 점
    if t == 0 or t == 1:
        for _, y in locations:
            for row in range(4, N):
                if board[row][y]:
                    max_row = max(max_row, row - 1)
                    break

        for _, y in locations:
            board[max_row][y] = True

    else:
        lower_row, lower_col = locations[-1]
        for row in range(4, N):
            if board[row][lower_col]:
                max_row = row - 1
                break
        for x, y in locations[::-1]:
            board[max_row][y] = True
            max_row -= 1


def drop_right(t):
    pass
    # max_col = -1
    # if t == 0 or t == 2:
    #     for x, _ in locations:
    #         for col in range(4, N):
    #             if board[x][col]:
    #                 max_col = max(max_col, col - 1)
    #                 break
    #     for x, _ in locations:
    #         board[x][max_col] = True
    #
    # else:
    #     right_row, right_col = locations[-1]
    #     for col in range(4, N):
    #         if board[right_row][col]:
    #             max_col = col - 1
    #             break
    #     for x, y in locations[::-1]:
    #         board[x][max_col] = True
    #         max_col -= 1


def check_row():
    pass


def check_light_yellow():
    pass


def check_col():
    pass


def check_light_red():
    pass


def simulate(t, x, y):
    for dx, dy in types[t]:
        nx, ny = x + dx, y + dy
        locations.append((nx, ny))
        
    # 도형을 아래로 최대한 떨군다
    drop_down(t)
    # 도형을 오른쪽으로 최대한 떨군다
    drop_right(t)
    # 꽉 찬 행이 있다면 해당 행을 삭제하고 아래로 하나씩 떨군다
    check_row()
    # 연한 노란색 영역 확인하여 해당 행만큼 삭제 후 떨구기
    check_light_yellow()
    # 꽉 찬 열이 있다면 해당 열을 삭제하고 오른쪽으로 하나씩 떨군다
    check_col()
    # 연한 빨간색 영역 확인하여 해당 열만큼 삭제 후 떨구기
    check_light_red()

# MAIN
k = int(input())
for _ in range(k):
    t, x, y = tuple(map(int, input().split()))
    t -= 1
    simulate(t, x, y)

for row in board:
    for elem in row:
        print(elem, end=' ')
    print()