def solution(sizes):

    max_width = -1
    max_height = -1

    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0], sizes[i][1] = sizes[i][1], sizes[i][0]

        max_width = max(max_width, sizes[i][0])
        max_height = max(max_height, sizes[i][1])

    return max_width * max_height


print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))