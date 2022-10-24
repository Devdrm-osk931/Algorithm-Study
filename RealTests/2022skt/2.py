import sys
sys.setrecursionlimit(10**9)
answer = -1
max_case = -1


def dfs(receive, sell, result, day):
    global answer, max_case
    n = len(receive)
    # receive, sell, result에 따라 값을 갱신해본다
    if len(result) == day:
        case_answer = 0

        daily_stock = [
        [0 for _ in range(day + 1)]
        for _ in range(n)
        ]

        for day in range(1, day + 1):
            for i in range(n):
                # 입고를 받는다
                daily_stock[i][day] = daily_stock[i][day - 1] + receive[i][day - 1]

                # 가능한 모든 판매요구를 수용한다            
                if daily_stock[i][day] >= sell[i][day - 1]:
                    daily_stock[i][day] -= sell[i][day - 1]
                else:
                    daily_stock[i][day] = 0

            # 다음 날로 넘어가기 전 result의 결과에 따라 최대한 구매를 한다
            case_answer += daily_stock[result[day - 1]][day]
            daily_stock[result[day - 1]][day] = 0

        # 최대 케이스를 갱신해준다
        if case_answer >= max_case:
            max_case = case_answer
            answer = result[:]
        return

    for i in range(n - 1, -1, -1):
        result.append(i)
        dfs(receive, sell, result, day)
        result.pop()


def solution(receive, sell):
    global answer
    n = len(receive)
    day = 5 
    dfs(receive, sell, [], 5)
    return answer