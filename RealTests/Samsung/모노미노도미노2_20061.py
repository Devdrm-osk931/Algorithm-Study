N = 10
types = [
    [(0, 0)],
    [(0, 0), (0, 1)],
    [(0, 0), (1, 0)]
]

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





def simulate(t, x, y):
    # 도형을 아래로 최대한 떨군다

    # 도형을 오른쪽으로 최대한 떨군다

    # 꽉 찬 행이 있다면 해당 행을 삭제하고 아래로 하나씩 떨군다

    # 연한 노란색 영역 확인하여 해당 행만큼 삭제 후 떨구기

    # 꽉 찬 열이 있다면 해당 열을 삭제하고 오른쪽으로 하나씩 떨군다

    # 연한 빨간색 영역 확인하여 해당 열만큼 삭제 후 떨구기


# MAIN
k = int(input())
for _ in range(k):
    t, x, y = tuple(map(int, input().split()))
    simulate(t, x, y)
