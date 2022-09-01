# BOJ 2559 수열

n, k = tuple(map(int, input().split()))
seq = list(map(int, input().split()))

# 두 종류의 포인터 선언
p1 = 0
p2 = k

k_sum = sum(seq[p1:p2])
answer = k_sum

while p2 < n:
    p2 += 1
    k_sum = k_sum + seq[p2 - 1] - seq[p1]
    answer = max(answer, k_sum)
    p1 += 1


print(answer)