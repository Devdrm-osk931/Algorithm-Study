def solution(n):
    mem = [0] * (n + 1)
    mem[0], mem[1] = 0, 1

    for i in range(2, n + 1):
        mem[i] = (mem[i - 2] + mem[i - 1]) % 1234567

    return mem[n]