n = int(input())
customers = list(map(int, input().split()))
leader, member = tuple(map(int, input().split()))
ans = 0
for customer in customers:
    ans += 1
    remainder = 0 if customer <= leader else customer - leader

    if remainder <= 0:
        continue

    ans += (remainder // member)
    if remainder % member == 0:
        continue
    else:
        ans += 1

print(ans)
