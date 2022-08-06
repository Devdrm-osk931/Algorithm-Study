from math import *

UP = (-1, 0)
DOWN = (1, 0)
RIGHT = (0, 1)
LEFT = (0, -1)

def print_answer(array):
    print("CHECK")
    for row in array:
        for elem in row:
            print(elem, end=' ')
        print()


def in_range(nx, ny, limit):
    return 0 <= nx < limit and 0 <= ny < limit


def solution(n, horizontal):
    answer = [
        [0 for _ in range(n)]
        for _ in range(n)
    ]

    if horizontal:
        # 오른쪽, 아래, 왼쪽, 아래, 오른쪽, 위
        movements = [RIGHT, DOWN, LEFT, DOWN, RIGHT, UP]
    else:
        # 아래, 오른쪽, 위, 오른쪽 , 아래, 왼쪽
        movements = [DOWN, RIGHT, UP, RIGHT, DOWN, LEFT]

    # 첫번째 위치 처리
    curr_x, curr_y = 0, 0
    movement_num = 0

    for i in range(1, n*n + 1):
        # 현재 위치 처리
        answer[curr_x][curr_y] = i

        # 새로운 위치 갱신
        limit = ceil(sqrt(i + 1))
        new_x, new_y = curr_x + movements[movement_num][0], curr_y + movements[movement_num][1]
        if not in_range(new_x, new_y, limit):
            movement_num = (movement_num + 1) % 6
            new_x, new_y = curr_x + movements[movement_num][0], curr_y + movements[movement_num][1]
        curr_x, curr_y = new_x, new_y

    return answer

solution(5, False)