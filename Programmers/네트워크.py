def dfs(start, n, visited, computers):
    
    # start+1번 노드부터 탐색하기
    for i in range(0, n):
        if computers[start][i] == 1 and not visited[i]:
            # 새로운 노드 탐색
            visited[start] = True
            dfs(i, n, visited, computers)

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(len(computers))]

    for v in range(len(visited)):
        # 노드 방문 기록이 없다면
        if not visited[v]:
            answer += 1
            dfs(v, n, visited, computers)
    return answer