def solution(array, commands):
    answer = []
    for i, j, k in commands:
        temp_array = array[i-1:j]
        temp_array.sort()
        print(temp_array)
        answer.append(temp_array[k-1])
    return answer