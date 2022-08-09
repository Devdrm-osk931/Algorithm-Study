def solution(money):
    cnt = len(money)

    dp1 = [money[0], money[0]] + ([0] * (cnt - 2))  # 첫번째 요소를 선택하는 경우
    dp2 = [0, money[1]] + ([0] * (cnt - 2))  # 첫번째 요소를 선택하지 않는 경우

    for i in range(2, cnt - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])
    for i in range(2, cnt):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + money[i])

    return max(dp1[-2], dp2[-1])

solution([1,2,3,1])