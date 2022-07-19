from collections import deque

def solution(maps):
    # queue for DFS
    q = deque()

    # row, col value of maps
    row = len(maps)
    col = len(maps[0])

    # array to store minimum distance to (m , n)
    dist = [
        [0] * col
        for _ in range(row)
    ]

    # E, S, W, N
    #                (row - 1, col)
    #  (row, col - 1)  (row, col)  (row, col + 1)
    #                (row + 1, col)
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    q.append((0, 0))
    dist[0][0] = 1

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < row and 0 <= ny < col and not dist[nx][ny] and (nx, ny) != (0, 0) and maps[nx][ny]:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1

    return dist[row - 1][col - 1] if dist[row - 1][col - 1] != 0 else -1


print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))