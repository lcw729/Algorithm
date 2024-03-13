def solution(numbers, target):
    global answer
    answer = 0
    
    DFS(numbers, target, 0 + numbers[0], 0)
    DFS(numbers, target, 0 - numbers[0], 0)    
    
    return answer

def DFS(numbers, target, result, depth):
    global answer

    if depth == len(numbers) - 1:
        if (result == target):
            answer = answer + 1
        return;
    
    DFS(numbers, target, result + numbers[depth+1], depth+1)
    DFS(numbers, target, result - numbers[depth+1], depth+1)
    