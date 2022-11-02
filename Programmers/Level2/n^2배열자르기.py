# Programmers
# n^2 배열 자르기 Lv2

# 주어진 값의 범위가 10^7 로 매우 커서 완탐 풀이는 시간초과가 발생
# 2차원 배열의 규칙을 이용하여 해결

def compute(row, col):
    if col < row + 1:
        return row + 1
    else:
        return col + 1


def solution(n, left, right):
    answer = []

    for idx in range(left, right + 1):
        idx_row, idx_col = idx // n, idx % n

        answer.append(compute(idx_row, idx_col))

    return answer

# 1 2 3
# 2 2 3
# 3 3 3

# 1 2 3 4
# 2 2 3 4
# 3 3 3 4
# 4 4 4 4

# 1 2 3 4 5
# 2 2 3 4 5
# 3 3 3 4 5
# 4 4 4 4 5
# 5 5 5 5 5