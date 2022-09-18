# BOJ 19237 어른상어 골드2
# Samsung

N, M, k = tuple(map(int, input().split()))

# 위 아래 왼쪽 오른쪽
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
elapsed_time = 0

sharks = [
    list(map(int, input().split()))
    for _ in range(N)
]

curr_dir = list(map(int, input().split()))

# 상어 번호 N이고 방향아 d 라면 우선순위는 -> priority[N - 1][d - 1]
priority = [
    [
        list(map(int, input().split()))
        for _ in range(4)
    ]
    for _ in range(k)
]


"""
def simulate():
    # 1000초까지 시뮬레이션을 진행한다
    while elapsed_time < 1000:
        if done():
            return elapsed_time
        move_all()

    return -1
"""