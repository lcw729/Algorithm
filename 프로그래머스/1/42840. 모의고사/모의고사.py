def solution(answers):
    answer = []
    one_pattern = [1,2,3,4,5]
    two_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    three_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    scores = [score(answers, one_pattern), 
              score(answers, two_pattern), 
              score(answers, three_pattern)]
    for i, value in enumerate(scores):
        if value == max(scores):
            answer.append(i + 1)
    
    return answer

def score(answers, pattern):
    pattern = pattern * ((len(answers) // len(pattern)) + 1)
    count = 0
    for i in range(len(answers)):
        if pattern[i] == answers[i]:
            count += 1
    
    return count
            