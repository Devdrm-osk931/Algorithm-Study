# BOJ 2775
# 부녀회장이 될테야

tc = int(input())

for _ in range(tc):
    k = int(input())
    n = int(input())  # n호까지 있음

    people = [
        [i for i in range(1, n + 1)]
    ]

    for _ in range(k):
        people.append([0 for _ in range(n)])

    for floor in range(1, k + 1):
        for i in range(n):
            people[floor][i] = sum(people[floor - 1][:i + 1])

    print(people[k][n - 1])
