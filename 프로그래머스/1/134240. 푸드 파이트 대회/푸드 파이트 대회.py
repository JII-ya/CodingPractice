def solution(food):
    answer = ''
    for i in range(len(food)):
        left = food[i] // 2
        answer += str(i) * left
    return answer +'0' + answer[::-1]