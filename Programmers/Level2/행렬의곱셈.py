# Programmers
# 행렬의 곱셈

def solution(arr1, arr2):
    # 결과물 배열의 크기 -> len(arr1) * len(arr2[0])
    answer = [
        [0 for _ in range(len(arr2[0]))]
        for _ in range(len(arr1))
    ]

    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            # arr1의 i번째 행과 arr2의 j번째 열
            r = arr1[i]
            c = [arr2[a][j] for a in range(len(arr2))]

            for x, y in zip(r, c):
                answer[i][j] += x * y

    return answer
