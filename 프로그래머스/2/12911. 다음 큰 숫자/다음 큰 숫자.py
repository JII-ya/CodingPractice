def solution(n):
    ct1 = bin(n).count('1')
    
    while True:
        n += 1
        if ct1 == bin(n).count('1'):
            break
            
    return n