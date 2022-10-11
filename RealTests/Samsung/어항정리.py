# BOJ 어항정리 플레1
# Samsung
from collections import deque

BLANK = 0
MAX = 100
n, k = tuple(map(int, input().split()))

numbers = [deque(map(int, input().split()))]

# 상 좌 하 우
dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def increase_min_by_one():
    min_val = min(numbers[0])

    for i in range(n):
        if numbers[0][i] == min_val:
            numbers[0][i] += 1


def lavitate1():
    # 맨 처음 요소를 위에 올려놓는다
    numbers.append(deque([numbers[0].popleft()]))
    while len(numbers) <= len(numbers[0]) - len(numbers[-1]):
        total_length = len(numbers)
        last_length = len(numbers[-1])
        target = []
        for col in range(last_length - 1, -1, -1):
            case_row = []
            for row in range(total_length):
                case_row.append(numbers[row][col])
            target.append(case_row)
        # 배열의 총 길이보다 1번 작은만큼 numbers를 팝한다
        for _ in range(total_length - 1):
            numbers.pop()
        # 마지막 길이만큼 1층을 pop한다
        for _ in range(last_length):
            numbers[0].popleft()

        for floor in target:
            numbers.append(deque(floor))


def lavitate2():
    while len(numbers[-1]) > n // 4:
        total_length = len(numbers)
        last_length = len(numbers[-1])
        target = []

        for row in range(total_length):
            case_row = []
            for col in range(last_length // 2):
                case_row.append(numbers[row][col])
            target.append(case_row)

        for row in numbers:
            for _ in range(last_length // 2):
                row.popleft()

        while target:
            next = target.pop()[::-1]
            numbers.append(deque(next))


def adjust():
    cnt = max(len(numbers[0]), len(numbers))
    # 임시 배열
    temp = [
        [0 for _ in range(cnt)]
        for _ in range(cnt)
    ]


    # numbers 정보를 temp로 옮겨준다
    for row in range(cnt):
        for col in range(cnt):
            try:
                temp[row][col] = numbers[row][col]
            except:
                continue

    # numbers를 순회하며 인접한 칸과 마릿수를 비교한다
    for row in range(cnt):
        for col in range(cnt):
            cx, cy = row, col
            for dx, dy in zip(dxs, dys):
                nx, ny = cx + dx, cy + dy
                try:
                    if numbers[cx][cy] > numbers[nx][ny] and cx >= 0 and cy >= 0 and nx >= 0 and ny >= 0:
                        diff = (numbers[cx][cy] - numbers[nx][ny]) // 5
                        if diff > 0:
                            temp[cx][cy] -= diff
                            temp[nx][ny] += diff
                except:
                    continue

    # 온도 조정이 된 임시 배열을 다시 원 배열로 옮겨준다
    for row in range(cnt):
        for col in range(cnt):
            try:
                numbers[row][col] = temp[row][col]
            except:
                continue


# 쌓아둔 배열을 다시 1열로 펴준다
def flatten():
    global numbers
    temp = deque()
    for col in range(len(numbers[0])):
        for row in range(len(numbers)):
            try:
                temp.append(numbers[row][col])
            except:
                break
    numbers = [temp]


def simulate():
    cnt = 0
    # 0. 맨 처음에 이미 최대/최소 차이가 K 이하라면
    min_val, max_val = min(numbers[0]), max(numbers[0])
    if max_val - min_val <= k:
        print(max_val, min_val)
        print(cnt)
        return

    while abs(min(numbers[0]) - max(numbers[0])) > k:
        # 1. 최소 물고기 하나 증가시키기
        increase_min_by_one()

        # 2. 공중부양 작업 - 90도, 조절
        lavitate1()
        adjust()

        # 3. 일렬로 재배열한다
        flatten()

        # 4. 공중부양 작업 - 180도
        lavitate2()
        adjust()

        # 5. 일렬로 재배치한다
        flatten()
        cnt += 1

    print(cnt)

simulate()