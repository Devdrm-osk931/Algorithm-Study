def solution(s):
    answer = True
    p_cnt = 0
    y_cnt = 0

    for char in s:
        if char.lower() == 'p':
            p_cnt += 1
        elif char.lower() == 'y':
            y_cnt += 1

    return True if p_cnt == y_cnt else False