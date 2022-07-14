equations = list(input().split('-'))
values = []

for equation in equations:
    value = 0
    temp = equation.split("+")
    for num in temp:
        value += int(num)
    values.append(value)

answer = values[0]

for idx in range(1, len(values)):
    answer -= values[idx]

print(answer)