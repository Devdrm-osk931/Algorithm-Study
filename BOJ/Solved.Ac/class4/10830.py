n, exp = tuple(map(int, input().split()))


def int_and_mod(n):
    return int(n) % 1000


matrix = [
    list(map(int_and_mod, input().split()))
    for _ in range(n)
]


def multiply(arr1, arr2):
    result = [
        [0] * n
        for _ in range(n)
    ]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += arr1[i][k] * arr2[k][j]
            result[i][j] = result[i][j] % 1000

    return result


def power(arr, n):
    if n == 1:
        return arr
    else:
        tmp = power(arr, n//2)
        if n % 2 != 0:
            return multiply(multiply(tmp, tmp), arr)
        else:
            return multiply(tmp, tmp)


answer = power(matrix, exp)
for row in answer:
    for elem in row:
        print(elem, end=' ')
    print()