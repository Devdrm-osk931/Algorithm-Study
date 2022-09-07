# BOJ 17140 골드4
# Samsung

r, c, k = tuple(map(int, input().split()))

numbers = [
    list(map(int, input().split()))
    for _ in range(3)
]


def same_or_more_rows():
    return len(numbers) >= len(numbers[0])


def sort_by_row():
    global numbers
    temp = []
    for row in numbers:
        next_row = []
        num_cnt = {}
        for num in row:
            if num == 0:
                continue
            if num in num_cnt:
                num_cnt[num] += 1
            else:
                num_cnt[num] = 1

        for key, value in num_cnt.items():
            next_row.append((key, value))
        next_row.sort(key=lambda x:(x[1], x[0]))

        new_row = []
        for num, frequency in next_row:
            new_row.append(num)
            new_row.append(frequency)
        temp.append(new_row)

    max_length = 0
    for row in temp:
        max_length = max(max_length, len(row))
    for row in temp:
        for _ in range(max_length - len(row)):
            row.append(0)

    numbers = [
        row[:]
        for row in temp
    ]


def sort_by_col():
    transpose()
    sort_by_row()
    transpose()


def transpose():
    global numbers
    temp = []
    for col in zip(*numbers):
        temp.append(list(col))
    numbers = [
        row[:]
        for row in temp
    ]


def in_range(x, y):
    row_cnt = len(numbers)
    col_cnt = len(numbers[0])
    return 0 <= x < row_cnt and 0 <= y < col_cnt


def simulate():
    target_row, target_col = r - 1, c - 1

    try:
        if numbers[target_row][target_col] == k:
            print(0)
            return
    except:
        pass

    for answer in range(1, 101):
        if same_or_more_rows():
            sort_by_row()
        else:
            sort_by_col()

        if in_range(target_row, target_col):
            if numbers[target_row][target_col] == k:
                print(answer)
                return
    print(-1)
    return

simulate()