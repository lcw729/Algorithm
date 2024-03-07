def solution(sizes):
    answer = 0
    w_max = 0;
    h_max = 0;
    for i, size in enumerate(sizes):
        [w, h] = size
        if w < h: w, h = h, w
        w_max = max(w_max,w)
        h_max = max(h_max,h)
            
    answer = w_max * h_max
        
    return answer