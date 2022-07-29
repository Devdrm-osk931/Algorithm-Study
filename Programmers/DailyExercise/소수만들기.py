def solution(nums):
    answer = 0
    combination = []
    
    def is_prime(n):
        for div in range(2, int(n ** (1/2)) + 1):
            if n % div == 0:
                return False
        return True
    
    def dfs(depth, arr):
        nonlocal combination, answer
        if depth == 3:
            if is_prime(sum(combination)):
                print(combination)
                answer += 1
            return
        
        for i in range(len(arr)):
            combination.append(arr[i])
            dfs(depth + 1, arr[:i] + arr[i + 1:])
            combination.pop()
        
    dfs(0, nums)
            
    return answer/6