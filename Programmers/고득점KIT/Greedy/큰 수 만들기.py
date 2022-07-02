def solution(number, k):
    answer = ''
    k = len(number) - k
    base = 0
    for limit in range(k):
        temp = number[base:len(number) - (k - limit - 1)]
        max = "0"
        max_idx = 0

        for idx in range(len(temp)):
            if (temp[idx]) > max:
                max = temp[idx]
                max_idx = idx
        answer += str(max)
        base += max_idx + 1
    return answer