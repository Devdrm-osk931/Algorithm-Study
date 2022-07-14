# BOJ_1946_신입사원_실버1

import sys
si = sys.stdin.readline

tc = int(si())

for i in range(tc):
    n = int(si())
    people = [
        list(map(int, si().split()))
        for _ in range(n)
    ]

    ans = 1
    people.sort()
    MAX = people[0][1]

    for idx in range(1, n):
        if people[idx][1] < MAX:
            ans += 1
            MAX = people[idx][1]
    print(ans)