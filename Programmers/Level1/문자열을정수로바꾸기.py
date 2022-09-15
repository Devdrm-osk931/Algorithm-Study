def solution(s):
    if s[0] == '+' or s[0] == '-':
        sign = s[0]
        number = int(s[1:])
        return number if sign == '+' else -1 * number
    else:
        number = s
        return int(number)