def solution(s):
    answer = 0
    def is_valid(s):
        stack = []
        pair = {')': '(', ']': '[', '}': '{'}
        
        for i in s:
            if i in '([{':
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1] != pair[i]:
                    return False
                stack.pop()
        return not stack

    for j in range(len(s)):
        rotated = s[j:] + s[:j]
        if is_valid(rotated):
            answer += 1
    return answer