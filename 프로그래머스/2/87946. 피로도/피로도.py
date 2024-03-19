from itertools import permutations

def solution(k, dungeons):
    global answer
    global visited
    
    answer = 0
    visited = [0 for i in range(len(dungeons)+1)]
    dfs(k, 0, dungeons)
        
    return answer

def dfs(pirodo, cnt, dungeons):
    global answer
    if cnt > answer:
        answer = cnt
    for idx, dungeon in enumerate(dungeons):
        [minimum, consume] = dungeon
        if (not visited[idx]) and pirodo >= minimum:
            visited[idx] = 1
            dfs(pirodo - consume, cnt + 1, dungeons);
            visited[idx] = 0