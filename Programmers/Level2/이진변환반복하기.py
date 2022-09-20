def solution(s):
    answer = []
    transform_cnt = 0
    removed_zeroes = 0

    while s != "1":
        transform_cnt += 1
        # s 에서 모든 0을 제외한다
        s = list(s)
        for i in range(len(s)):
            if s[i] == "0":
                removed_zeroes += 1
                s[i] = ""
        s = "".join(s)

        # s의 길이를 구한다
        s_length = len(s)
        print(s_length)

        binary = []
        # s_length에 해당하는 숫자를 2진수로 나타내어 s에 할당한다
        while s_length > 0:
            binary.append(str(s_length % 2))
            s_length //= 2
        binary = binary[::-1]

        s = "".join(binary)

    return [transform_cnt, removed_zeroes]