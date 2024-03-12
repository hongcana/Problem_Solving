
N, M = map(int, input().split(" "))
land = [list(map(int, input().split(" "))) for _ in range(N)]

K = int(input())
query = [list(map(int, input().split(" "))) for _ in range(K)]

for i in range(len(land)):
    if i == 0:
        for j in range(1, len(land[i])):
            land[0][j] += land[0][j-1] 
    else:
        land[i][0] += land[i-1][0]
        for j in range(1, len(land[i])):
            land[i][j] = land[i][j] + land[i-1][j] + land[i][j-1] - land[i-1][j-1]

print(land)
print(query)

for q in query:
    x1, y1, x2, y2 = q[0], q[1], q[2], q[3]

    if x1 == 1 and y1 == 1:
        print(land[x2-1][y2-1])
    elif x1 == 1 and y1 != 1:
        print(land[x2-1][y2-1] - land[x2-1][y1-2]) # 2,3  2,2
    elif x1 != 1 and y1 == 1:
        print(land[x2-1][y2-1] - land[x1-2][y2-1])
    else:
        print(land[x2-1][y2-1] - land[x1-2][y2-1] - land[x2-1][y1-2] + land[x1-2][y1-2])

    # 293 - 148 - 110 + 55
    # => (x2,y2) - (3,1) - (1,3) + (1,1)
    # 1 2 3 4 = (3,4)에서 (3,1) 값을 빼면 됨, 182
    # 1 3 3 4 = (3,4)에서 (3,2) 값을 빼면 됨, 111
    # 1 4 3 4 = 36
    # 2 1 3 4
    # 2 2 3 4 = (3,4)에서 (1,3), (1,4) 값을 빼고 (1,1)을 더해주면 됨
    # 3 3 4 4 = (4,4)에서 (2,4), (4,2) 값을 빼고 (2,2)를 더해주면 됨