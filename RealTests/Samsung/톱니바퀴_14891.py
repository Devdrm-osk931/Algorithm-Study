N, M = 4, 8
CW, CCW, NONE = 1, -1, 0
rotate_dirs = [0] * N

tables = [
    list(input())
    for _ in range(N)
]


def flip(dir):
    return CW if dir == CCW else CCW

def rotate(table_num, rotate_dir):
    if rotate_dir == CW:
        temp = tables[table_num][M - 1]

        for idx in range(M - 1, 0, -1):
            tables[table_num][idx] = tables[table_num][idx - 1]
        tables[table_num][0] = temp
    
    else:
        temp = tables[table_num][0]
        for idx in range(0, M-1):
            tables[table_num][idx] = tables[table_num][idx + 1]
        tables[table_num][M - 1] = temp


def simulate(table_num, spin_direction):
    global rotate_dirs

    # initialize rotate_dirs
    rotate_dirs = [NONE for _ in range(N)]

    # 시작 테이블 기록
    rotate_dirs[table_num - 1] = spin_direction

    # 시작 테이블 기준 왼쪽 테이블들의 회전 방향 결정 table_num - 2 ~ 0
    for table in range(table_num - 2, -1, -1):
        print(tables[table][2], tables[table + 1][6])
        if tables[table][2] != tables[table_num][6]:
            rotate_dirs[table] = flip(rotate_dirs[table + 1])
        else:
            break
    
    for table in range(table_num, N):
        print(tables[table][6])
        print(tables[table - 1][2])
        if tables[table][6] != tables[table - 1][2]:
            rotate_dirs[table] = flip(rotate_dirs[table - 1])
        else:
            break
    
    print(rotate_dirs)
    table = 0
    for rotate_dir in rotate_dirs:
        rotate(table, rotate_dir)
        table += 1
        

    


k = int(input())
for _ in range(k):
    table, spin_dir = tuple(map(int, input().split()))
    simulate(table, spin_dir)

for row in tables:
    for elem in row:
        print(elem, end=' ')
    print()