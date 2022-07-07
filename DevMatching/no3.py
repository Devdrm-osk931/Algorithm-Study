from collections import deque

OCEAN = 1
LAND = 2
LAKE = 0
lake_area = 1


def in_range(x, y, row, col):
    return 0 <= x < row and 0 <= y < col


def dfs(area, start_node, row, col):
    curr_x, curr_y = start_node
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        new_x = curr_x + dx
        new_y = curr_y + dy
        if in_range(new_x, new_y, row, col):
            if area[new_x][new_y] == 0:
                area[new_x][new_y] = 1
                dfs(area, (new_x, new_y), row, col)


def get_area_by_dfs(area, start_node, row, col, cnt):
    global lake_area
    curr_x, curr_y = start_node
    dxs = [0, 1, 0, -1]
    dys = [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        new_x = curr_x + dx
        new_y = curr_y + dy
        if in_range(new_x, new_y, row, col):
            if area[new_x][new_y] == 0:
                area[new_x][new_y] = 3
                lake_area += 1
                get_area_by_dfs(area, (new_x, new_y), row, col, cnt)
    return cnt


def solution(rows, columns, lands):
    global lake_area
    answer = []

    # 전체 영역
    area = [
        [0 for _ in range(columns)]
        for _ in range(rows)
    ]

    # 땅 표시
    for row, col in lands:
        area[row-1][col-1] = LAND

    # 바다 식별 - (0, 0)을 시작으로 하는 DFS
    curr_x, curr_y = 0, 0
    dfs(area, (curr_x, curr_y), rows, columns)

    # 호수가 존재한다면 넓이 구하기
    EXIST = False
    lake_areas = []
    for row in range(rows):
        for col in range(columns):
            if area[row][col] == 0:
                lake_area = 1
                EXIST = True
                get_area_by_dfs(area, (row, col), rows, columns, 1)
                print(lake_area)

    print(area)


    return answer
