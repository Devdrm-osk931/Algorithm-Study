# Samsung
# 연산자 끼워넣기 (Silver1)

n = int(input())
nums = list(map(int, input().split()))
first = nums[0]
nums = nums[1:]
ops = list(map(int, input().split()))
max_val, min_val = -1e9, 1e9

result = []


def compute():
    evaluation = first
    for i in range(n - 1):
        if result[i] == 0:
            evaluation += nums[i]
        elif result[i] == 1:
            evaluation -= nums[i]

        elif result[i] == 2:
            evaluation *= nums[i]

        else:
            if evaluation < 0:
                evaluation = evaluation * (-1)
                evaluation //= nums[i]
                evaluation = evaluation * (-1)
            else:
                evaluation //= nums[i]
        # print(evaluation, end=' ')
    # print()
    return evaluation


def pick(cnt):
    global max_val, min_val
    if cnt == n - 1:
        case_val = compute()
        # print(result, case_val)
        max_val = max(max_val, case_val)
        min_val = min(min_val, case_val)
        return

    for op in range(4):
        if ops[op] > 0:
            result.append(op)
            ops[op] -= 1
            pick(cnt + 1)
            op = result.pop()
            ops[op] += 1

pick(0)
print(max_val)
print(min_val)
# 1, 3, 0, 0, 2