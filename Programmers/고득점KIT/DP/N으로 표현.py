def solution(N, number):
    LIMIT = 8
    dp = [
        set()
        for _ in range(LIMIT + 1)
    ]

    for i in range(1, LIMIT + 1):
        dp[i].add(int(str(N) * i))

        if i >= 2:
            for subidx in range(1, i):
                for item1 in dp[subidx]:
                    for item2 in dp[i - subidx]:
                        dp[i].add(item1 + item2)
                        dp[i].add(item1 - item2)
                        dp[i].add(item1 * item2)
                        if item2 != 0:
                            dp[i].add(item1//item2)

        if number in dp[i]:
            return i

    return -1

print(solution(5, 12))