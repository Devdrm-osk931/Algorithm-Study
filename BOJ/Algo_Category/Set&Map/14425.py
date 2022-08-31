# BOJ 14425 문자열 집합

n, m = tuple(map(int, input().split()))
S = set()
answer = 0

for _ in range(n):
    string = input()
    S.add(string)

for _ in range(m):
    check = input()
    if check in S:
        answer += 1

print(answer)