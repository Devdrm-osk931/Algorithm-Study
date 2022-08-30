n, L = tuple(map(int, input().split()))

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

arr = [0 for _ in range(n)]
ramp_cnt = [0 for _ in range(n)]


# [a, b] 구간의 숫자가 모두 동일한지확인
def all_same(a, b):
    return len(set(arr[a:b + 1])) == 1


# 통과가 가능한 길인지 확인
def can_pass():
    global ramp_cnt

    for i in range(n - 1):
        if abs(arr[i] - arr[i + 1]) >= 2:
            return False

    # ramp_cnt 배열 초기화
    ramp_cnt = [0 for _ in range(n)]

    # 높->아래 형태의 경사로가 필요한 지점
    for i in range(n - 1):
        # [i + 1, i + L] 까지 경사로 필요
        if arr[i] == arr[i + 1] + 1:
            if i + L >= n:
                return False

            if not all_same(i + 1, i + L):
                return False

            for j in range(i + 1, i + L + 1):
                ramp_cnt[j] = 1

    # 아래 -> 높 형태의 경사로가 필요한 지점
    for i in range(1, n):
        # [i - L, i - 1]
        if arr[i] == arr[i-1] + 1:
            if i - L < 0:
                return False

            if not all_same(i - L, i - 1):
                return False

            for j in range(i - L, i):
                ramp_cnt[j] += 1

    if any([cnt >= 2 for cnt in ramp_cnt]):
        return False
    return True


ans = 0

# 각 행 검사
for row in range(n):
    for col in range(n):
        arr[col] = grid[row][col]
    if can_pass():
        ans += 1

# 각 열 검사
for col in range(n):
    for row in range(n):
        arr[row] = grid[row][col]
    if can_pass():
        ans += 1

print(ans)
