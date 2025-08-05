def solution(s):
    a = 0
    b = 0
    
    while s != "1":
        b += s.count("0")
        s = s.replace("0",'')
        s = bin(len(s))[2:]
        a += 1
        
    return [a,b]