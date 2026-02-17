def solution(elements):
    n = len(elements)
    arr = elements *2
    
    psum = [0] * (2*n + 1)
    for i in range(1, 2*n + 1):
        psum[i] += arr[i-1] + psum[i-1]
    result = set()
    
    for j in range(1, n+1):
        for k in range(n):
            total = psum[j+k] - psum[k]
            result.add(total)
            
    return len(result)