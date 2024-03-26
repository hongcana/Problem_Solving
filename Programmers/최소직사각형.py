def solution(sizes):
    w_max, h_max = 0,0
    for i in range(len(sizes)):
        if sizes[i][1] > sizes[i][0] :
            tmp = sizes[i][1]
            sizes[i][1] = sizes[i][0]
            sizes[i][0] = tmp
        
        if sizes[i][0] > w_max:
            w_max = sizes[i][0]
        if sizes[i][1] > h_max:
            h_max = sizes[i][1]
    
    return w_max * h_max
