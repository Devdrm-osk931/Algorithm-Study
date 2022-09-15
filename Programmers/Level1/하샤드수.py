def solution(x):
    x_list = list(map(int, list(str(x))))
    digit_sum = sum(x_list)
    return True if x % digit_sum == 0 else False