# Samsung
# BOJ_3190_Gold4
from collections import deque

n = int(input())  # 격자의 크기
k = int(input())  # 사과의 갯수

BLANK = 0
SNAKE = 1
APPLE = 2

graph = [
    [BLANK for _ in range(n + 1)]
    for _ in range(n + 1)
]

# 사과
for _ in range(k):
    a, b = tuple(map(int, input().split()))
    graph[a][b] = APPLE

# 시간 별 움직임 변화 명령어
l = int(input())
cmds = dict()
for _ in range(l):
    time, command = input().split()
    time = int(time)
    cmds[time] = command


# 특정 좌표가 격자 안에 존재하는지 확인
def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n


def can_go(x, y):
    return in_range(x, y) and (graph[x][y] == BLANK or graph[x][y] == APPLE)


def change_direction(cmd):
    global dir_num
    if cmd == 'L':
        dir_num = (dir_num - 1) % 4
    else:
        dir_num = (dir_num + 1) % 4

# 뱀 관련 초기 설정 및 변수 설정
time = 0
dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 오른쪽, 아래, 왼쪽, 위
dir_num = 0  # 초기 방향은 오른쪽이다
positions = deque([(1, 1)])
graph[1][1] = SNAKE

while True:
    head_x, head_y = positions[-1]  # 뱀의 제일 앞부분의 좌표
    dx, dy = dirs[dir_num]  # 방향 dx, dy
    new_x, new_y = head_x + dx, head_y + dy  # 진행 방향으로 1만큼 증가시킨다
    time += 1  # 움직인 시점에 시간을 늘려준다

    if can_go(new_x, new_y):  # 만약 새로운 지점이 이동이 가능한 지점이라면 -> 벽도 아니고 내 몸의 일부도 아니라면
        if graph[new_x][new_y] == APPLE:
            # 사과를 섭취하고 팝을 수행하지 않는다
            graph[new_x][new_y] = SNAKE
        else:
            # 이동을 하고 꼬리에 있던 자리를 없애줌 - pop
            tail_x, tail_y = positions.popleft()
            graph[new_x][new_y] = SNAKE
            graph[tail_x][tail_y] = BLANK
        positions.append((new_x, new_y))

    else:
        break

    # 해당 시간에 방향을 바꿔야한다면 방향을 바꾼다
    if time in cmds:
        cmd = cmds[time]
        change_direction(cmd)

print(time)