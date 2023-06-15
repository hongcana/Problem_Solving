from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def solution(maps):
    """
    전형적인 BFS 풀이
    """
    visited = [[1 for _ in range(len(maps[0]))] for _ in range(len(maps))]
    q = deque([])
    q.append([0,0])
    
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0 <= nx < len(maps)) and (0 <= ny < len(maps[0])) and visited[nx][ny] == 1 and maps[nx][ny] == 1:
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx,ny])
            
            if (nx == len(maps) - 1) and (ny == len(maps[0]) -1):
                return visited[nx][ny]
    return -1