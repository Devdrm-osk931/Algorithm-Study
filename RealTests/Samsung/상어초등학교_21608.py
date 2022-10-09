# BOJ 상어초등학교 골드5
# Samsung

BLANK = 0

# 교실의 크기 => N * N
# 학생 수 => N * N
N = int(input())
student_cnt = N * N

seats = [
    [BLANK for _ in range(N)]
    for _ in range(N)
]

# 각 학생의 선호도
preference = {}

# 선호도 입력
for _ in range(student_cnt):
    a, b, c, d, e = tuple(map(int, input().split()))
    preference[a] = {b, c, d, e}

dxs = [-1, 0, 1, 0]
dys = [0, -1, 0, 1]


def in_range(x, y):
    return 0 <= x < N and 0 <= y < N


def place(student_num, student_preference):
    # 학생이 최종적으로 앉게 될 위치
    target_row, target_col = student_num, student_num
    prefer_cnt = -1
    zeroes = -1
    for x in range(N):
        for y in range(N):
            # 이미 선점된 자리는 패스
            if seats[x][y]:
                continue

            # 4방향을 살펴보며 선호하는 학생 수를 센다
            case_cnt = 0
            case_zero = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if not in_range(nx, ny):
                    continue
                if seats[nx][ny] in student_preference:
                    case_cnt += 1
                elif seats[nx][ny] == BLANK:
                    case_zero += 1
            # print(f"({x}, {y}) -> 선호칸: {case_cnt}, 빈 칸: {case_zero}")

            # 선호 칸이 가장 큰것으로 갱신해준다
            if case_cnt > prefer_cnt:
                target_row, target_col, prefer_cnt, zeroes = x, y, case_cnt, case_zero

            # 선호하는 칸 갯수가 같다면 비어있는 칸이 더 많은 쪽으로 갱신해준다
            elif case_cnt == prefer_cnt and zeroes < case_zero:
                target_row, target_col, prefer_cnt, zeroes = x, y, case_cnt, case_zero

            # 선호 칸과 빈칸 갯수가 같다면 행/열이 더 작은 쪽으로 갱신한다
            elif case_cnt == prefer_cnt and zeroes == case_zero and (target_row, target_col) > (x, y):
                target_row, target_col, prefer_cnt, zeroes = x, y, case_cnt, case_zero

    # 학생을 앉힌다
    seats[target_row][target_col] = student_num
    return target_row, target_col


def get_satisfaction():
    total_score = 0
    for x in range(N):
        for y in range(N):
            cnt = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = x + dx, y + dy
                if not in_range(nx, ny):
                    continue
                if seats[nx][ny] in preference[seats[x][y]]:
                    cnt += 1
            if cnt == 1:
                total_score += 1
            elif cnt == 2:
                total_score += 10
            elif cnt == 3:
                total_score += 100
            elif cnt == 4:
                total_score += 1000
    return total_score


def simulate():
    # 순서대로 학생을 앉힌다
    for student_num, student_preference in preference.items():
        place(student_num, student_preference)
    print(get_satisfaction())


simulate()
