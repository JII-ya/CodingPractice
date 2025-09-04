import math
def solution(n):
    root = math.sqrt(n)
    if root == int(root):
        answer = int((root+1)**2)
    else:
        answer = -1
    return answer