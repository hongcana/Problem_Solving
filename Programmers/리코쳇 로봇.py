from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(pos, board, visited):
    q = deque()
    q.append([pos[0],pos[1],0])
    while q:
        x,y,times = q.popleft()
        if board[x][y] == 'G':
            return times
        
        for i in range(4):
            # 상,하,좌,우 방향 결정
            nx = x
            ny = y

            # 상,하,좌,우 방향의 끝 점까지 이동
            while (0 <= nx+dx[i] < (len(board))) and (0 <= ny+dy[i] < (len(board[0]))) and board[nx+dx[i]][ny+dy[i]] != "D":
                nx += dx[i]
                ny += dy[i]

            # 끝점 방문
            if (0 <= nx < (len(board))) and (0 <= ny < (len(board[0]))) and visited[nx][ny] == 0:
                visited[nx][ny] = times+1
                q.append([nx,ny, visited[nx][ny]])
    return -1

def solution(board):
    """
    약~간 변형된 BFS문제.
    끝점까지 밀고나간다는 점이 다름.
    그리고 끝점까지 밀고 나가니까 nx = x+ dx[i]를 딱히 해줄 필요도 없음
    현재 코드에서 만약 nx = x + dx[i]로 해서 진행한다면, 순간이동이 되어버려서 코드를 약간 바꿔줘야함.
    visited를 inf로 초기화해서 최초 방문을 최소값으로 처리하여 진행하는 방법도 있긴하나...
    0으로 초기화해서 최초 방문 = 최소 접근으로 처리해도 무방할듯(해당 문제에서는)
    """
    answer = 0
    visited = [[0] * len(board[0]) for _ in range(len(board))]

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'R':
                answer = bfs([i,j], board, visited)
    
    return answer

if __name__=="__main__":
    print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))