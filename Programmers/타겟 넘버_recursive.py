
def solution(numbers, target):
    answer = 0
    
    # +1 -> +1 -> +1 -> +1 -> +1 ... 깊이 우선 탐색 (재귀)
    def dfs(num, i):
        # 끝까지 가라
        tmp = 0
        if i != (len(numbers)-1):
            tmp += dfs(num + numbers[i+1],i+1)
            tmp += dfs(num - numbers[i+1],i+1)
        
        # else: 만약 끝까지 갔다. 그리고 target과 같으면..
        else:
            if num == target:
                return 1
            else:
                return 0
        return tmp
        
    def start_dfs(num, i, ans):
        ans += dfs(num, i)
        ans += dfs(-num, i)
        return ans

    answer = start_dfs(numbers[0],0, 0)
    return answer