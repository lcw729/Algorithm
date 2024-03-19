from itertools import permutations

def solution(k, dungeons):
    maximum = 0
    result = 0
    
    nPr = permutations(dungeons, len(dungeons))
    for current in list(nPr):
        result = completion(k, current)
        if (result > maximum):
            maximum = result
        
    return maximum

def completion(k, dungeons):
    count = 0
    for dungeon in dungeons:
        [minimun, consume] = dungeon
        if (minimun > k or consume > k):
            return count
        k = k - consume
        count = count + 1
    return count