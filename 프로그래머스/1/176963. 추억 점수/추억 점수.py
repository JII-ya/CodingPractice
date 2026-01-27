def solution(name, yearning, photo):
    answer = []
    dict_name={}
    for a,b in zip(name, yearning):
        dict_name[a]=b
        
    for i in photo:
        score = 0
        for j in i:
            score += dict_name.get(j, 0)
        answer.append(score)
    return answer