from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(pos, visited, maps, target):
    q = deque()
    q.append([pos[0],pos[1]])

    while q:
        x, y = q.popleft()
        
        # 레버 찾기
        if target == 'lever' and maps[x][y] == 'L':
            return visited[x][y]
        elif target == 'end' and maps[x][y] == 'E':
            return visited[x][y]
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < len(maps)) and (0 <= ny < len(maps[0])) and (maps[nx][ny] != "X") and visited[nx][ny] == 0 :
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx,ny])
    return -1
                

def solution(maps):
    '''
    bfs를 두번 돌려서 풀이했던 문제. 레버까지 bfs -> 레버에서 끝점까지 bfs
    미로의 행과 열이 일치하지 않다는게 포인트. visited 조건을 달리해야함.
    '''
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == 'S':
                pos_x, pos_y = i,j
            elif maps[i][j] == 'L':
                pos_lx, pos_ly = i,j
    
    # 레버 까지 거리 구하는 BFS
    answer = bfs([pos_x,pos_y], visited, maps, 'lever')
    
    # 레버를 찾았다면, visited 초기화
    if answer != -1:
        visited = [[0] * len(maps[0]) for _ in range(len(maps))]
        
        # 레버 찾은 이후 출구 찾는 BFS
        answer_end = bfs([pos_lx,pos_ly], visited, maps, 'end')
        if answer_end == -1:
            answer = -1
        else:
            answer += answer_end
            
    return answer

if __name__=="__main__":
    print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))