# 고속 거듭제곱 알고리즘

a, b, c = tuple(map(int, input().split()))

def fast_power(base, exp):
    if exp == 1:
        return base % c
    else:
        tmp = fast_power(base, exp//2)
        if exp % 2 == 0:
            return (tmp * tmp) % c
        else:
            return (tmp * tmp * a) % c

print(fast_power(a, b))
