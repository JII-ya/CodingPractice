def solution(s):
    answer = int(len(s)/2)
    if len(s)%2 != 0:
        return s[answer]
    else:
        return s[answer-1:answer+1]