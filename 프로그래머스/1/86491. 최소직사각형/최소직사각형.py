def solution(sizes):
    arrange = [(max(x), min(x)) for x in sizes]
    
    max_1 = max(x[0] for x in arrange)
    max_2 = max(x[1] for x in arrange)
    
    return max_1*max_2