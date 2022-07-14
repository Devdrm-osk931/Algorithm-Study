# BOJ_2512_실버3

n = int(input())
budgets = list(map(int, input().split()))
total_budget = int(input())
budgets.sort()

# 총 요청 예산 합
req_budget = sum(budgets)

# 모든 예산 할당 가능 -> 최대 예산이 최대 가능 예산
if req_budget < total_budget:
    print(budgets[-1])

# 이진 탐색을 통해 최대값을 산정한다
else:
    # 0 ~ 150
    start, end = 0, budgets[-1]
    max_possible_budget = 0

    while start <= end:
        mid = (start + end) // 2
        case_sum = 0
        for request in budgets:
            if request > mid:
                case_sum += mid
            else:
                case_sum += request
        if case_sum <= total_budget:
            max_possible_budget = mid
            start = mid + 1
        else:
            end = mid - 1

    print(max_possible_budget)