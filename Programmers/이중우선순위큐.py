import heapq as hq

def solution(operations):
    answer = []
    minh = []
    maxh = []
    
    in_cnt = 0
    del_cnt = 0

    for o in operations:
        l = o.split(" ")
        oper, val = l[0], int(l[1])
        if oper == "I":
            hq.heappush(minh, val)
            hq.heappush(maxh, -val)
            in_cnt += 1
        
        elif oper == "D":
            # 빈 큐에 데이터를 삭제하라는 연산이 주어질 경우, 무시
            if len(minh) == 0 or len(maxh) == 0:
                continue 
            elif val == -1:
                hq.heappop(minh)
                del_cnt += 1
            elif val == 1:
                hq.heappop(maxh)
                del_cnt += 1
            if del_cnt == in_cnt:
                while len(minh) != 0:
                    hq.heappop(minh)
                while len(maxh) != 0:
                    hq.heappop(maxh)
    if del_cnt == in_cnt:
        return [0,0]
    else:
        print(del_cnt, in_cnt)
        return [-maxh[0], minh[0]]
    
    return answer