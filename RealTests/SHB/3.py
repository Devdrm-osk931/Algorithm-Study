import math

def solution(n):
    answer = 0
    outer_period = int(math.log10(n))
    inner_period = int('1' * (outer_period + 1))
    add_amount = n // inner_period


    if 5 <= add_amount < 9:
        add_amount -= 1
    elif add_amount >= 9:
        add_amount -= 2


    return outer_period * 8 + add_amount
