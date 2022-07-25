def solution(board, moves):
    answer = 0
    stack = []

    N = len(board)
    
    for move in moves:
        col = move - 1
        for row in range(N):
            if board[row][col]:
                stack.append(board[row][col])
                board[row][col] = 0
                while len(stack) >= 2 and stack[-1] == stack[-2]:
                    answer += 2
                    stack.pop()
                    stack.pop()
                break
        
    return answer