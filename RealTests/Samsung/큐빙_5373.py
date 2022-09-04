Up = [
    ['w' for _ in range(3)]
    for _ in range(3)
]

Down = [
    ['y' for _ in range(3)]
    for _ in range(3)
]

Front = [
    ['r' for _ in range(3)]
    for _ in range(3)
]

Back = [
    ['o' for _ in range(3)]
    for _ in range(3)
]

Left = [
    ['g' for _ in range(3)]
    for _ in range(3)
]

Right = [
    ['b' for _ in range(3)]
    for _ in range(3)
]

Up_copied = [
    ['w' for _ in range(3)]
    for _ in range(3)
]

Down_copied = [
    ['y' for _ in range(3)]
    for _ in range(3)
]

Front_copied = [
    ['r' for _ in range(3)]
    for _ in range(3)
]

Back_copied = [
    ['o' for _ in range(3)]
    for _ in range(3)
]

Left_copied = [
    ['g' for _ in range(3)]
    for _ in range(3)
]

Right_copied = [
    ['b' for _ in range(3)]
    for _ in range(3)
]


def init():
    global Up, Down, Front, Back, Left, Right
    Up = [row[:] for row in Up_copied]
    Down = [row[:] for row in Down_copied]
    Front = [row[:] for row in Front_copied]
    Back = [row[:] for row in Back_copied]
    Left = [row[:] for row in Left_copied]
    Right = [row[:] for row in Right_copied]


def spin(face, direction):
    # 앞 뒤 왼 오 면의 변화
  화 if face == 'U':
        if direction == '+':


    elif face == 'D':

    elif face == 'F':

    elif face == 'B':

    elif face == 'L':

    else:


tc = int(input())
for _ in range(tc):
    init()
    n = int(input())
    cmds = list(input().split())
    for cmd in cmds:
        face, direction = cmd[0], cmd[1]
        spin(face, direction)
