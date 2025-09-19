def solution(arr):
    answer = []
    for i, val in enumerate(arr):
        if i==0 or val!=arr[i-1]:
            answer.append(val)
    return answer