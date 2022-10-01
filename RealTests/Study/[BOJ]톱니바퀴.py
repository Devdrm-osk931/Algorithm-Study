# BOJ 톱니바퀴 골5
# Samsung

from collections import deque

CW = 1
CCW = -1
NOT_ROTATE = 0
N = 4

gears = [0 for _ in range(N + 1)]
rotate_dirs = [0] + [NOT_ROTATE for _ in range(N)]

# 톱니바퀴 극 정보를 받아준다
for idx in range(1, N + 1):
    gear = deque(list(input()))
    gears[idx] = gear


def init_rotate_dirs():
    for i in range(1, N + 1):
        rotate_dirs[i] = NOT_ROTATE


def flip(i):
    return CW if rotate_dirs[i] == CCW else CCW


def set_rotate_dirs(start, direction):
    # 시작 톱니바퀴의 회전 방향을 정해준다
    rotate_dirs[start] = direction

    # 시작 톱니바퀴 이전의 톱니바퀴들 방향을 정해준다
    for i in range(start - 1, 0, -1):
        # 인접한 톱니바퀴 극이 다른 경우 반대 방향으로 바꾼다
        if gears[i][2] != gears[i + 1][6]:
            rotate_dirs[i] = flip(i + 1)
        else:
            break

    # 시작 톱니바퀴 이후의 톱니바퀴들 방향을 정해준다
    for i in range(start + 1, N + 1):
        if gears[i][6] != gears[i - 1][2]:
            rotate_dirs[i] = flip(i - 1)
        else:
            break


# 시뮬레이션 함수
def simulate(start, direction):
    # rotate_dirs 초기화
    init_rotate_dirs()

    # 회전할 방향을 정해준다
    set_rotate_dirs(start, direction)

    # 회전 방향으로 각 톱니바퀴를 회전시켜준다
    for gear_num in range(1, N + 1):
        if rotate_dirs[gear_num] == NOT_ROTATE:
            continue

        gears[gear_num].rotate(rotate_dirs[gear_num])


# k번의 회전을 한다
k = int(input())
for _ in range(k):
    gear_num, direction = tuple(map(int, input().split()))
    simulate(gear_num, direction)

# 점수 합산
answer = 0
for gear_num in range(1, N + 1):
    if gears[gear_num][0] == '1':
        answer += 2 ** (gear_num - 1)
print(answer)