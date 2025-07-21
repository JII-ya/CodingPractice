from collections import Counter
def solution(k, tangerine):
    answer = 0
    tan = Counter(tangerine)
    sort_tan = sorted(tan.items(), key=lambda x:x[1], reverse = True)
    
    cnt=0
    for i in sort_tan:
        k -= i[1]
        answer += 1
        if k <=0:
            break
    return answer