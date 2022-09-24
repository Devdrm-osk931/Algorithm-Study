BLANK = -1
N = 50

def solution(commands):
    answer = []
    merge_idx = 1

    grid = [
        [-1 for _ in range(N)]
        for _ in range(N)
    ]

    merged = [
        [False for _ in range(N)]
        for _ in range(N)
    ]

    og_value = [
        [-1 for _ in range(N)]
        for _ in range(N)
    ]

    for command in commands:
        command = command.split(" ")

        # Update의 2가지 케이스
        if command[0] == "UPDATE":
            if len(command) == 4:
                r, c = int(command[1]) - 1, int(command[2]) - 1
                value = command[3]

                idx = merged[r][c]
                if idx:
                    for i in range(N):
                        for j in range(N):
                            if merged[i][j] == idx:
                                grid[i][j] = value
                else:
                    grid[r][c] = value
            if len(command) == 3:
                find = command[1]
                value = command[2]
                for i in range(N):
                    for j in range(N):
                        if grid[i][j] == find:
                            if merged[i][j]:
                                for x in range(N):
                                    for y in range(N):
                                        if merged[x][y] == merged[i][j]:
                                            grid[x][y] = value
                            else:
                                grid[i][j] = value
        # Merge
        elif command[0] == "MERGE":
            r1, c1 = int(command[1]) - 1, int(command[2]) - 1
            r2, c2 = int(command[3]) - 1, int(command[4]) - 1
            new_value = ""

            # 병합될 값 판단
            val1 = grid[r1][c1]
            val2 = grid[r2][c2]
            if val1 and val2:
                new_value = val1
            elif val1 and not val2:
                new_value = val1
            elif not val1 and val2:
                new_value = val2
            else:
                new_value = BLANK
            # 병합처리
            group1 = merged[r1][c1]
            group2 = merged[r2][c2]

            # 두 셀 모두 병합되지 않았던 셀이라면
            if not group1 and not group2:
                merged[r1][c1] = merged[r2][c2] = merge_idx
                grid[r1][c1] = grid[r2][c2] = new_value

            elif group1 and not group2:
                # group1 에 속한 모든 값을 새로운 merge_idx로 바꿔준다
                for i in range(N):
                    for j in range(N):
                        if merged[i][j] == group1:
                            merged[i][j] = merge_idx
                            grid[i][j] = new_value

                # group2 도 바꿔준다
                merged[r2][c2] = merge_idx
                grid[r2][c2] = new_value

            elif not group1 and group2:
                merged[r1][c1] = merge_idx
                grid[r1][c1] = new_value

                for i in range(N):
                    for j in range(N):
                        if merged[i][j] == group2:
                            merged[i][j] = merge_idx
                            grid[i][j] = new_value
            else:
                for i in range(N):
                    for j in range(N):
                        if merged[i][j] == group1:
                            merged[i][j] = merge_idx
                            grid[i][j] = new_value
                        if merged[i][j] == group2:
                            merged[i][j] = merge_idx
                            grid[i][j] = new_value
            merge_idx += 1

        elif command[0] == "UNMERGE":
            r, c = int(command[1]) - 1, int(command[2]) - 1
            target_value = grid[r][c]
            case_merge_cnt = merged[r][c]

            for i in range(N):
                for j in range(N):
                    if merged[i][j] == case_merge_cnt:
                        merged[i][j] = False
                        grid[i][j] = BLANK
            grid[r][c] = target_value

        else:
            r, c = int(command[1]) - 1, int(command[2]) - 1
            if grid[r][c] == BLANK:
                answer.append("EMPTY")
            else:
                answer.append(grid[r][c])

    return answer


#
commands = ["UPDATE 1 1 a", "UPDATE 1 2 b", "UPDATE 2 1 c", "UPDATE 2 2 d", "MERGE 1 1 1 2","MERGE 2 2 2 1", "MERGE 2 1 1 1", "PRINT 1 1", "UNMERGE 2 2", "PRINT 1 1"]
print(solution(commands))