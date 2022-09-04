def solution(numbers):
    visited = [False] * 10
    
    for number in numbers:
        visited[number] = True
    
    
    return sum([
        i
        for i in range(10)
        if not visited[i]
    ])