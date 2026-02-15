def solution(n):
    a = ''
    while n > 0:
        a = str(n%3) + a
        n //= 3    
    b = a[::-1]
    answer = int(b, 3)
    return answer